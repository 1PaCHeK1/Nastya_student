from pydantic import BaseModel

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

class Product(BaseModel):
    id: int = None
    name: str 
    price: float
    picture: str = None
    volume: float 
    sale: int = None

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates('templates')


@app.get("/")
def read_root(request: Request, response_model=HTMLResponse) -> HTMLResponse:
    product1 = Product(id=1, name='kitket', price=500, volume=700, sale=15)
    product2 = Product(id=1, name='вискас', price=600, volume=900)

    return templates.TemplateResponse('welcome_page.html', 
                        {'request':request, 'items': [product1, product2]})


@app.get("/items/{item_id}/{date}/")
def read_item(item_id: int, date: str, q: str|None = None):
    return {"item_id": item_id, "q": q}


items = [
    {"item_id": 1, "q": 1},
    {"item_id": 2, "q": 2},
    {"item_id": 3, "q": 3},
]

@app.get("/items/")
def read_item():
    return items

print()