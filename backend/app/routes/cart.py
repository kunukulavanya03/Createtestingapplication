from fastapi import APIRouter
from app.database import engine
from app.models import Cart, Product

router = APIRouter()

@router.post("/api/cart")
def add_to_cart(product_id: int):
    cart = Cart(user_id=1)
    engine.execute(Cart.__table__.insert().values(user_id=cart.user_id))
    product = engine.execute(Product.__table__.select().where(Product.id == product_id)).first()
    return {"cart": cart, "products": product}