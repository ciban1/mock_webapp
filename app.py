from typing import Union, Dict, Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/home/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse("homepage.html", {"request": request, "id": id})

@app.get("/display/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse("displaypage.html", {"request": request, "id": id})

@app.get("/contact/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse("contactpage.html", {"request": request, "id": id})


# make each a dict with key of object, value of price
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

# inventory = {
#     "name": "Milk",
#     "price": 3.99,
#     "brand": "Cow"
# }
inventory = {}


@app.get("/cart/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse("shoppingcartpage.html", {"request": request, "id": id, "cart": inventory})

# # to insert item, need id associated with it
@app.post("/cart/create/{item_id}")
def create_cart(item_id: int, item: Item):  # sending item info in request body
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    # if inventory at item_id
    inventory[item_id] = item # access all fields of item
    return inventory[item_id]

# @app.get("/cart/{item_id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: int):
#     return templates.TemplateResponse("shoppingcartpage.html", {"request": request})

# @app.get("/cart/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: int, cart: Dict[str, None]):
#     return templates.TemplateResponse("shoppingcartpage.html", {"request": request, "id": id, "cart": cart})