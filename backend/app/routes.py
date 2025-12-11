from fastapi import APIRouter
from app.models import Test, Question, TestResult
from app.schemas import Test, Question, TestResult
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

tests_router = APIRouter()

@tests_router.post("/tests")
def create_test(test: TestBase):
    db = get_db()
    new_test = Test(name=test.name, description=test.description)
    db.add(new_test)
    db.commit()
    return new_test

@tests_router.get("/tests")
def get_tests():
    db = get_db()
    return db.query(Test).all()

@tests_router.get("/tests/{test_id}")
def get_test(test_id: int):
    db = get_db()
    return db.query(Test).filter(Test.id == test_id).first()

@tests_router.put("/tests/{test_id}")
def update_test(test_id: int, test: TestBase):
    db = get_db()
    updated_test = db.query(Test).filter(Test.id == test_id).first()
    updated_test.name = test.name
    updated_test.description = test.description
    db.commit()
    return updated_test

@tests_router.delete("/tests/{test_id}")
def delete_test(test_id: int):
    db = get_db()
    db.query(Test).filter(Test.id == test_id).delete()
    db.commit()
    return {"message": "Test deleted"}

questions_router = APIRouter()

@questions_router.post("/questions")
def create_question(question: QuestionBase):
    db = get_db()
    new_question = Question(text=question.text, test_id=question.test_id)
    db.add(new_question)
    db.commit()
    return new_question

@questions_router.get("/questions")
def get_questions():
    db = get_db()
    return db.query(Question).all()

@questions_router.get("/questions/{question_id}")
def get_question(question_id: int):
    db = get_db()
    return db.query(Question).filter(Question.id == question_id).first()

@questions_router.put("/questions/{question_id}")
def update_question(question_id: int, question: QuestionBase):
    db = get_db()
    updated_question = db.query(Question).filter(Question.id == question_id).first()
    updated_question.text = question.text
    updated_question.test_id = question.test_id
    db.commit()
    return updated_question

@questions_router.delete("/questions/{question_id}")
def delete_question(question_id: int):
    db = get_db()
    db.query(Question).filter(Question.id == question_id).delete()
    db.commit()
    return {"message": "Question deleted"}

test_results_router = APIRouter()

@test_results_router.get("/tests/{test_id}/results")
def get_test_results(test_id: int):
    db = get_db()
    return db.query(TestResult).filter(TestResult.test_id == test_id).all()
