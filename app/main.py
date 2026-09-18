from datetime import datetime, timezone
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.db.base import Base
from app.db.models import Course, KnowledgePoint, KnowledgeProgress, Lesson, Problem, Submission
from app.db.session import engine, get_db
from app.logging_config import configure_logging
from app.schemas.api import HintRequest, ReviewRequest, SubmissionCreate
from app.services.ai_review_service import get_ai_provider
from app.services.judge_service import judge

app = FastAPI(title="Python Developer Lab", version="0.1.0")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")


@app.on_event("startup")
def startup():
    configure_logging()
    Path("data").mkdir(exist_ok=True)
    Base.metadata.create_all(engine)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/courses")
def courses(db: Session = Depends(get_db)):
    rows = db.scalars(
        select(Course)
        .where(Course.is_active)
        .options(selectinload(Course.lessons).selectinload(Lesson.problems))
        .order_by(Course.sort_order)
    ).all()
    return [
        {
            "id": c.id,
            "code": c.code,
            "name": c.name,
            "description": c.description,
            "lessons": [
                {
                    "id": lesson.id,
                    "code": lesson.code,
                    "name": lesson.name,
                    "problems_count": len(lesson.problems),
                }
                for lesson in c.lessons
            ],
        }
        for c in rows
    ]


@app.get("/api/courses/{course_id}")
def course(course_id: int, db: Session = Depends(get_db)):
    c = db.scalar(
        select(Course)
        .where(Course.id == course_id)
        .options(selectinload(Course.lessons).selectinload(Lesson.problems))
    )
    if not c:
        raise HTTPException(404, "课程不存在")
    return {
        "id": c.id,
        "code": c.code,
        "name": c.name,
        "description": c.description,
        "lessons": [
            {
                "id": lesson.id,
                "code": lesson.code,
                "name": lesson.name,
                "problems": [
                    {"id": p.id, "code": p.code, "title": p.title, "difficulty": p.difficulty}
                    for p in lesson.problems
                ],
            }
            for lesson in c.lessons
        ],
    }


@app.get("/api/problems")
def problems(db: Session = Depends(get_db)):
    return [
        {
            "id": p.id,
            "code": p.code,
            "title": p.title,
            "difficulty": p.difficulty,
            "type": p.type,
            "lesson_id": p.lesson_id,
        }
        for p in db.scalars(
            select(Problem).where(Problem.is_active).order_by(Problem.sort_order)
        ).all()
    ]


@app.get("/api/problems/{problem_id}")
def problem(problem_id: int, db: Session = Depends(get_db)):
    p = db.scalar(
        select(Problem).where(Problem.id == problem_id).options(selectinload(Problem.test_cases))
    )
    if not p:
        raise HTTPException(404, "题目不存在")
    return {
        "id": p.id,
        "code": p.code,
        "title": p.title,
        "description": p.description,
        "input_spec": p.input_spec,
        "output_spec": p.output_spec,
        "constraints": p.constraints,
        "starter_code": p.starter_code,
        "difficulty": p.difficulty,
        "type": p.type,
        "expected_concepts": p.expected_concepts,
        "visible_tests": [
            {"input": t.input_data, "expected": t.expected_stdout}
            for t in p.test_cases
            if not t.is_hidden
        ],
    }


@app.post("/api/submissions")
def submit(payload: SubmissionCreate, db: Session = Depends(get_db)):
    p = db.scalar(
        select(Problem)
        .where(Problem.id == payload.problem_id)
        .options(selectinload(Problem.test_cases))
    )
    if not p:
        raise HTTPException(404, "题目不存在")
    result = judge(p, payload.code)
    s = Submission(
        problem_id=p.id,
        code=payload.code,
        status=result["status"],
        passed_count=result["passed"],
        total_count=result["total"],
        stdout=result["stdout"],
        stderr=result["stderr"],
        execution_ms=result["execution_ms"],
        hint_level=payload.hint_level,
        used_solution=payload.used_solution,
    )
    db.add(s)
    independent = not payload.used_solution and payload.hint_level < 3
    if independent:
        for concept in [x.strip() for x in p.expected_concepts.split(",") if x.strip()]:
            kp = db.scalar(select(KnowledgePoint).where(KnowledgePoint.code == concept))
            if kp:
                prog = db.scalar(
                    select(KnowledgeProgress).where(KnowledgeProgress.knowledge_point_id == kp.id)
                ) or KnowledgeProgress(
                    knowledge_point_id=kp.id, attempt_count=0, pass_count=0, status="unseen"
                )
                if prog.id is None:
                    db.add(prog)
                prog.attempt_count += 1
                prog.last_attempt_at = datetime.now(timezone.utc)
                if result["status"] == "PASSED":
                    prog.pass_count += 1
                    prog.status = "mastered" if prog.pass_count >= 2 else "practiced"
                    if prog.status == "mastered":
                        prog.mastered_at = datetime.now(timezone.utc)
                else:
                    prog.status = "learning"
    db.commit()
    db.refresh(s)
    response = {"submission_id": s.id, **result}
    if result["status"] == "PASSED":
        concept_codes = [x.strip() for x in p.expected_concepts.split(",") if x.strip()]
        knowledge = db.scalars(
            select(KnowledgePoint).where(KnowledgePoint.code.in_(concept_codes))
        ).all()
        response["reference_solution"] = p.solution_code
        response["knowledge_explanation"] = [
            {"name": point.name, "description": point.description}
            for point in knowledge
        ]
    return response


@app.get("/api/submissions/{submission_id}")
def get_submission(submission_id: int, db: Session = Depends(get_db)):
    s = db.get(Submission, submission_id)
    if not s:
        raise HTTPException(404, "提交不存在")
    return {
        "id": s.id,
        "problem_id": s.problem_id,
        "status": s.status,
        "passed": s.passed_count,
        "total": s.total_count,
        "stdout": s.stdout,
        "stderr": s.stderr,
        "execution_ms": s.execution_ms,
    }


@app.get("/api/progress")
def progress(db: Session = Depends(get_db)):
    total = db.scalar(select(func.count(Problem.id))) or 0
    passed = (
        db.scalar(
            select(func.count(func.distinct(Submission.problem_id))).where(
                Submission.status == "PASSED"
            )
        )
        or 0
    )
    rows = db.scalars(
        select(KnowledgeProgress).options(selectinload(KnowledgeProgress.knowledge_point))
    ).all()
    return {
        "total_problems": total,
        "completed_problems": passed,
        "knowledge_mastered": sum(x.status == "mastered" for x in rows),
        "knowledge": [
            {
                "code": x.knowledge_point.code,
                "name": x.knowledge_point.name,
                "status": x.status,
                "attempt_count": x.attempt_count,
            }
            for x in rows
        ],
    }


@app.post("/api/ai/hint")
async def hint(payload: HintRequest, db: Session = Depends(get_db)):
    p = db.get(Problem, payload.problem_id)
    if not p:
        raise HTTPException(404, "题目不存在")
    return await get_ai_provider().generate_hint(p, payload.code, payload.level, {})


@app.post("/api/ai/review")
async def review(payload: ReviewRequest, db: Session = Depends(get_db)):
    p = db.get(Problem, payload.problem_id)
    if not p:
        raise HTTPException(404, "题目不存在")
    return await get_ai_provider().review_submission(p, payload.code, payload.judge_result)


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"courses": db.scalars(select(Course).order_by(Course.sort_order)).all()},
    )


@app.get("/problems/{problem_id}", response_class=HTMLResponse)
def problem_page(problem_id: int, request: Request, db: Session = Depends(get_db)):
    p = db.get(Problem, problem_id)
    if not p:
        raise HTTPException(404)
    next_problem = db.scalar(
        select(Problem)
        .where(Problem.is_active, Problem.sort_order > p.sort_order)
        .order_by(Problem.sort_order)
        .limit(1)
    )
    return templates.TemplateResponse(
        request=request,
        name="problem.html",
        context={"problem": p, "next_problem": next_problem},
    )
