from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, nullable=False)
    payment_method = Column(String, nullable=False)

    def __init__(self, cart_id, payment_method):
        self.cart_id = cart_id
        self.payment_method = payment_method