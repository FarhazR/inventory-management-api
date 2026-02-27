from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
from uuid import uuid4

app = FastAPI(title="Inventory Management API")

inventory: Dict[str, dict] = {}


class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "price": 59999.99,
                "quantity": 10
            }
        }


@app.get("/")
def root():
    return {"message": "Inventory API is running"}


@app.post("/products")
def add_product(product: Product):
    product_id = str(uuid4())
    inventory[product_id] = product.dict()
    return {"product_id": product_id, "product": inventory[product_id]}


@app.get("/products")
def get_all_products():
    return inventory


@app.get("/products/{product_id}")
def get_product(product_id: str):
    if product_id not in inventory:
        raise HTTPException(status_code=404, detail="Product not found")
    return inventory[product_id]


@app.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    if product_id not in inventory:
        raise HTTPException(status_code=404, detail="Product not found")
    inventory[product_id] = product.dict()
    return {"message": "Product updated", "product": inventory[product_id]}


@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in inventory:
        raise HTTPException(status_code=404, detail="Product not found")
    del inventory[product_id]
    return {"message": "Product deleted"}
