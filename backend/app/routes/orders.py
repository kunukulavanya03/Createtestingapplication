from fastapi import APIRouter
from app.database import engine
from app.models import Order, Cart

router = APIRouter()

@router.post("/api/orders")
def create_order(cart_id: int):
    order = Order(cart_id=cart_id, payment_method="example_payment")
    engine.execute(Order.__table__.insert().values(cart_id=order.cart_id, payment_method=order.payment_method))
    return {"order": order}

@router.get("/api/orders")
def get_orders():
    orders = engine.execute(Order.__table__.select()).fetchall()
    return {"orders": orders}