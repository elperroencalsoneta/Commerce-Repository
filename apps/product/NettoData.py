from bs4 import BeautifulSoup
import requests
import json
import psycopg2
from price_parser import Price
from datetime import datetime

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}

url = 'https://www.netto-online.de/lebensmittel/c-N01/'
response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")

product_titles = data.findAll(name="div", class_="product__title__inner")
product_prices = data.findAll(name="span", class_="product__current-price--digits-before-comma")
Div = data.findAll(name="div", class_="product__tile__img")
images = data.findAll(name="img", class_="product__image")
div2 = data.findAll(name="div", class_= "product__price-wrapper__inner")


# for div in div2:
#     element = div.find("del")
#     if element is not None:
#         print(element.find("span").get_text())

        
# for n in Div:
#     print(n)

total_information = {}
for n in range(1, 2):
    url =  f'https://www.netto-online.de/lebensmittel/c-N01/{n}'
    response = requests.get(url)
    data = BeautifulSoup(response.text, "html.parser")
    product_titles = data.findAll(name="div", class_="product__title__inner")
    product_old_price = data.findAll(name="del", class_="product__old-price")

    for n in range (len(product_titles) - 1):
            element = div2[n].find("del")
            if element is not None:
                element = element.find("span").get_text()
          
    

            total_information[len(total_information)] = {
                        "model": "product.product",
                        "pk": len(total_information) +  1,
                        "fields":
                    {
                        "name": product_titles[n].get_text(),
                        "photo": images[n]['data-src'],
                        "description": "This is a product",
                        "price": Price.fromstring(product_prices[n].get_text()).amount_float,
                        "compare_price": 80.52,
                        "category": 2,
                        "quantity": 0,
                        "sold": 80,
                        # "date_created": date.today().strftime("%Y-%m-%d"),
                        "date_created": "2022-12-26T11:55:38Z",
                        "in_offer": False,
                        # "Supermarket": "Netto"
                        # "date_created": "Hola"
                        }
                    }

Structured_Information = json.dumps(total_information, indent=4)
data = json.loads(Structured_Information)

conn = psycopg2.connect(database="E-Commerce", user="postgres", password="Punkhazard4!", host="localhost", port="5432")
cur = conn.cursor()

products = [v for k, v in data.items()]
Structured_Data = json.dumps(products, indent=4)
print(Structured_Data)
# for n in range(1, 28):
#     url = f'https://www.netto-online.de/lebensmittel/c-N01/{n}'
    

