from fastapi import FastAPI
from app.routes import auth, products, cart, orders
from app.database import engine
from app.config import settings

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Create the database tables
    engine.create_all()

@app.on_event("shutdown")
def shutdown_event():
    # Close the database connection
    engine.dispose()

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)