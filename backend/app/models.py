from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base, engine

Base.metadata.create_all(engine)

class Calculation(Base):
  __tablename__ = "calculations"
  id = Column(Integer, primary_key=True)
  operation = Column(String)
  num1 = Column(Float)
  num2 = Column(Float)
  result = Column(Float)