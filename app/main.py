from pydantic import BaseModel
from random import randint
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

class Product(BaseModel):
    id: int = None
    name: str 
    price: float
    picture: str = None
    volume: float = None
    pet: str
    sale: int = 0

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates('templates')


def json_information(file):
    products_information = open(file, 'r')
    products_information = json.load(products_information)
    products = {}
    for id, pr_inf in products_information.items():
        if pr_inf['pet'] not in products:
            products[pr_inf['pet']] = []
        product = Product(id=id, 
                        name=pr_inf['name'], 
                        price=pr_inf['price'], 
                        volume=pr_inf['volume'] if 'volume' in pr_inf else 0, 
                        sale=pr_inf['sale'], 
                        picture='images/' + pr_inf['pet'] + '/' + pr_inf['image']+'.jpg', 
                        pet=pr_inf['pet'])
        products[pr_inf['pet']].append(product)
    return products


def random_information():
    products = {'cats':[], 'dogs':[], 'birds':[], 'rodents':[]}
    pets=['dogs', 'cats', 'rodents', 'birds']
    for i in range(1, randint(1, 10)):
        pet = pets[randint(0, 3)]
        p = Product(id=str(i), 
                    name='товар ' + str(i), 
                    price=randint(100, 2000), 
                    volume=randint(0, 2000), 
                    picture='images/product.jpg',
                    sale=randint(0, 50), 
                    pet=pet)
        products[pet].append(p)
    return products

@app.get("/")
def read_root(request: Request, response_model=HTMLResponse) -> HTMLResponse:
    # из файла

    return templates.TemplateResponse('welcome_page.html', {'request':request, 
                                    'items':json_information('app/products.json')})

    # рандомная
    return templates.TemplateResponse('welcome_page.html', {'request':request, 
                                                            'items':random_information()})
