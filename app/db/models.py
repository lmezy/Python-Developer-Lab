from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


def now():
    return datetime.now(timezone.utc)


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text, default="")
    level: Mapped[str] = mapped_column(String(30), default="beginner")
    sort_order: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=now, onupdate=now)
    lessons: Mapped[list["Lesson"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )


class Lesson(Base):
    __tablename__ = "lessons"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    code: Mapped[str] = mapped_column(String(30), unique=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text, default="")
    sort_order: Mapped[int] = mapped_column(default=0)
    estimated_minutes: Mapped[int] = mapped_column(default=30)
    course: Mapped[Course] = relationship(back_populates="lessons")
    problems: Mapped[list["Problem"]] = relationship(
        back_populates="lesson", cascade="all, delete-orphan"
    )


class KnowledgePoint(Base):
    __tablename__ = "knowledge_points"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(120))
    category: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text, default="")
    prerequisite_ids: Mapped[str] = mapped_column(Text, default="")
    progress: Mapped["KnowledgeProgress|None"] = relationship(
        back_populates="knowledge_point", uselist=False
    )


class Problem(Base):
    __tablename__ = "problems"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(160))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    difficulty: Mapped[int] = mapped_column(default=1)
    type: Mapped[str] = mapped_column(String(20), default="BASIC")
    description: Mapped[str] = mapped_column(Text)
    input_spec: Mapped[str] = mapped_column(Text, default="")
    output_spec: Mapped[str] = mapped_column(Text, default="")
    constraints: Mapped[str] = mapped_column(Text, default="")
    starter_code: Mapped[str] = mapped_column(Text, default="")
    expected_concepts: Mapped[str] = mapped_column(Text, default="")
    hint_0: Mapped[str] = mapped_column(Text, default="")
    hint_1: Mapped[str] = mapped_column(Text, default="")
    hint_2: Mapped[str] = mapped_column(Text, default="")
    hint_3: Mapped[str] = mapped_column(Text, default="")
    solution_code: Mapped[str] = mapped_column(Text, default="")
    sort_order: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    lesson: Mapped[Lesson] = relationship(back_populates="problems")
    test_cases: Mapped[list["TestCase"]] = relationship(
        back_populates="problem", cascade="all, delete-orphan"
    )
    submissions: Mapped[list["Submission"]] = relationship(back_populates="problem")


class TestCase(Base):
    __tablename__ = "test_cases"
    id: Mapped[int] = mapped_column(primary_key=True)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    input_data: Mapped[str] = mapped_column(Text, default="")
    expected_stdout: Mapped[str] = mapped_column(Text)
    expected_exit_code: Mapped[int] = mapped_column(default=0)
    is_hidden: Mapped[bool] = mapped_column(Boolean, default=False)
    sort_order: Mapped[int] = mapped_column(default=0)
    problem: Mapped[Problem] = relationship(back_populates="test_cases")


class Submission(Base):
    __tablename__ = "submissions"
    id: Mapped[int] = mapped_column(primary_key=True)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    code: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30))
    passed_count: Mapped[int] = mapped_column(default=0)
    total_count: Mapped[int] = mapped_column(default=0)
    stdout: Mapped[str] = mapped_column(Text, default="")
    stderr: Mapped[str] = mapped_column(Text, default="")
    execution_ms: Mapped[int] = mapped_column(default=0)
    hint_level: Mapped[int] = mapped_column(default=0)
    used_solution: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)
    problem: Mapped[Problem] = relationship(back_populates="submissions")


class KnowledgeProgress(Base):
    __tablename__ = "knowledge_progress"
    id: Mapped[int] = mapped_column(primary_key=True)
    knowledge_point_id: Mapped[int] = mapped_column(ForeignKey("knowledge_points.id"), unique=True)
    status: Mapped[str] = mapped_column(String(20), default="unseen")
    attempt_count: Mapped[int] = mapped_column(default=0)
    pass_count: Mapped[int] = mapped_column(default=0)
    last_attempt_at: Mapped[datetime | None] = mapped_column(DateTime)
    mastered_at: Mapped[datetime | None] = mapped_column(DateTime)
    knowledge_point: Mapped[KnowledgePoint] = relationship(back_populates="progress")
