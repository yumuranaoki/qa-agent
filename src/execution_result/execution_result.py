from pydantic import BaseModel


class ExecutionResult(BaseModel):
    is_success: bool
    usability_feedback: str
