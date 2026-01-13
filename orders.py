
from fastapi import APIRouter
from app.database import SessionLocal
from app.crud import place_order

router=APIRouter(prefix='/orders')

@router.post('/place')
def order(data:dict):
    db=SessionLocal()
    return place_order(db,data)
