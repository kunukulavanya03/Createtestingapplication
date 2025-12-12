from fastapi import APIRouter
from app.database import engine
from app.models import Product

router = APIRouter()

@router.get("/api/products")
def get_products():
    products = engine.execute(Product.__table__.select()).fetchall()
    return {"products": products}

@router.get("/api/products/{id}")
def get_product(id: int):
    product = engine.execute(Product.__table__.select().where(Product.id == id)).first()
    return {"product": product}