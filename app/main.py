
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!!!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int = None, q: str|None = None):
    return {"item_id": item_id, "q": q}

items = [
    {"item_id": 1, "q": 1},
    {"item_id": 2, "q": 2},
    {"item_id": 3, "q": 3},
]

@app.get("/items/")
def read_item():
    return items