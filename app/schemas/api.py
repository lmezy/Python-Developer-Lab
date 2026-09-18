from pydantic import BaseModel, Field


class SubmissionCreate(BaseModel):
    problem_id: int
    code: str = Field(min_length=1, max_length=50000)
    hint_level: int = Field(default=0, ge=0, le=4)
    used_solution: bool = False


class HintRequest(BaseModel):
    problem_id: int
    code: str = ""
    level: int = Field(default=0, ge=0, le=3)


class ReviewRequest(BaseModel):
    problem_id: int
    code: str
    judge_result: dict
