
from fastapi import APIRouter
from app.database import SessionLocal
from app.crud import add_product

router=APIRouter(prefix='/products')

@router.post('/add')
def create(data:dict):
    db=SessionLocal()
    return add_product(db,data)
