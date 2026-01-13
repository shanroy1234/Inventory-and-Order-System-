
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from app.database import Base

class Product(Base):
    __tablename__='products'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    stock=Column(Integer)
    price=Column(Float)

class Order(Base):
    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    product_id=Column(Integer,ForeignKey('products.id'))
    quantity=Column(Integer)
    total_price=Column(Float)

class Supplier(Base):
    __tablename__='suppliers'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    contact=Column(String)
