from pydantic import BaseModel


class ExecutionInput(BaseModel):
    preparation: str
    steps: str
    expected_result: str
