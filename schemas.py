
from pydantic import BaseModel

class ProductIn(BaseModel):
    name:str
    stock:int
    price:float

class OrderIn(BaseModel):
    product_id:int
    quantity:int
