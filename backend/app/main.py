from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Settings
from app.database import engine, Base, SessionLocal
from app.models import Calculation

app = FastAPI()

@app.get("/arithmetic/{{operation}}")
def calculate(operation: str, num1: float, num2: float):
  if operation == '+':
    result = num1 + num2
  elif operation == '-':
    result = num1 - num2
  elif operation == '*':
    result = num1 * num2
  elif operation == '/':
    if num2 != 0:
      result = num1 / num2
    else:
      return JSONResponse(content={'error': 'Cannot divide by zero'}, status_code=400)
  else:
    return JSONResponse(content={'error': 'Invalid operation'}, status_code=400)

  calculation = Calculation(operation=operation, num1=num1, num2=num2, result=result)
  session = SessionLocal()
  session.add(calculation)
  session.commit()
  session.close()

  return {'result': result}

@app.post("/input")
def validate_input(input: str):
  try:
    operation, num1, num2 = input.split()
    num1, num2 = float(num1), float(num2)
    if operation not in ['+', '-', '*', '/']:
      return {'valid': False, 'error': 'Invalid operation'}
    if operation == '/' and num2 == 0:
      return {'valid': False, 'error': 'Cannot divide by zero'}
    return {'valid': True, 'error': ''}
  except ValueError:
    return {'valid': False, 'error': 'Invalid input'}

@app.get("/data")
def get_data():
  session = SessionLocal()
  data = session.query(Calculation).all()
  session.close()
  return {'data': [calc.__dict__ for calc in data]}