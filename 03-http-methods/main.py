from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Optional
app = FastAPI(
    title="Basic HTTP Methods",
    description="Practice HTTP methods, GET, POST, PUT, POST",
    version="0.116.0"
)

class Item(BaseModel):
    id:int
    name:str
    price:int
    is_available:Optional[bool] = True

items:list[Item] = []

@app.get("/get-items")
def get_items():
    return items

@app.post("/add-item")
def add_item(item:Item):
    items.append(item)
    return {"message":f"{item.name} added!"}

@app.put("/update-item")
def update_item(item_id:int, updated_item:Item):
    for index,item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return f"Item updated by id {item_id}"

    raise HTTPException(status_code=400, detail="Item not found")
    
@app.delete("/delete-item")
def delete_item(item_id:int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return f"Item with id {item_id} removed!"
        
    raise HTTPException(status_code=400, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
