
from app.models import Product,Order

def add_product(db,data):
    p=Product(**data)
    db.add(p);db.commit();db.refresh(p);return p

def place_order(db,data):
    product=db.query(Product).get(data['product_id'])
    product.stock-=data['quantity']
    total=data['quantity']*product.price
    o=Order(product_id=product.id,quantity=data['quantity'],total_price=total)
    db.add(o);db.commit();db.refresh(o);return o
