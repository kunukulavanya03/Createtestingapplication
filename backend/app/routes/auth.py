from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import engine
from app.models import User
from app.config import settings

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/api/auth/register")
def register(user_data: User):
    user = User(username=user_data.username, email=user_data.email, password=user_data.password)
    engine.execute(User.__table__.insert().values(username=user.username, email=user.email, password=user.password))
    return {"token": "example_token"}

@router.post("/api/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = engine.execute(User.__table__.select().where(User.username == form_data.username)).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": "example_token"}