
from fastapi import FastAPI
from app.routers import products, orders, suppliers

app = FastAPI(title="Inventory & Order Management System")

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(suppliers.router)

@app.get("/")
def root():
    return {"message":"Inventory System Running"}
