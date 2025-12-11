from fastapi import FastAPI
from dotenv import load_dotenv
from app.config import settings
from app.routes import tests_router, questions_router, test_results_router

load_dotenv()
app = FastAPI()

app.include_router(tests_router)
app.include_router(questions_router)
app.include_router(test_results_router)
