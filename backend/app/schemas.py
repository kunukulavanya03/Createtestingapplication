from pydantic import BaseModel

class TestBase(BaseModel):
    name: str
    description: str | None = None

class Test(TestBase):
    id: int

class QuestionBase(BaseModel):
    text: str
    test_id: int

class Question(QuestionBase):
    id: int

class TestResultBase(BaseModel):
    test_id: int
    question_id: int
    answer: str

class TestResult(TestResultBase):
    id: int
