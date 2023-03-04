from bs4 import BeautifulSoup
import requests
import datefinder
from dateparser.search import search_dates
from datetime import date
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from dateparser.search import search_dates
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.firefox.options import Options


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}

offers = ["https://www.lidl.de/c/billiger-frische/a10007140#10072119", "https://www.lidl.de/c/billiger-frische/a10007140#10072123", "https://www.lidl.de/c/billiger-frische/a10007140#10063484", "https://www.lidl.de/c/billiger-frische/a10007140#10068000", 'https://www.lidl.de/c/billiger-montag/a10006065?channel=store&tabCode=Current_Sales_Week', "https://www.lidl.de/c/bad-ab-09-01/a10016781?channel=store&tabCode=Current_Sales_Week"]



headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}

firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))

for offer in offers:
    driver.get(offer)

    titles = driver.find_elements(By.CLASS_NAME, "grid-box__headline grid-box__text--dense")
    for title in titles:
        print(title.text)

#     elements = data.find_all(["a", "span", "button"], text=re.compile(r"Erlauben", re.IGNORECASE))
# DETERMINE IF THERE ARE COOKIES BUTTON


# for offer_response in product_sortiment_list:
#     response = requests.get(offer_response)
#     data = BeautifulSoup(response.text, "html.parser")
#     product_titles = data.findAll(name="h4", class_="m-offer-tile__title")
#     product_prices = data.findAll(name="div", class_="a-pricetag__price")
#     product_imageDiv = data.findAll(name="div", class_="m-offer-tile__image")
#     uncleancategory = data.find(name="h1", class_="a-headline")
#     pages_number = data.find(name="ul", class_="m-pagination__list")
#     category = ""
#     # if uncleancategory is not None:
#     #     category = uncleancategory.text.strip()
#     #     print(category)
#     # else:
#     #     category = "Unknown"
#     if pages_number is None:
#         print("You have to take the data normally")
#     if pages_number is not None:
#         number_of_pages = int(pages_number.findAll("li")[-2].getText().strip())
#         counter = 0
#         for page in range(0, number_of_pages - 1):
#             counter += 1
#             new_url = offer_response.replace(".html", "") + f".pageIndex={counter}.html"
#             response = requests.get(new_url)
            
#             for n in range (len(product_prices) - 1):
#                 total_information[len(total_information) + n] = {
#                         "model": "product.product",
#                         "pk": len(total_information) +  n,
#                         "fields":
#                     {
#                         "name": product_titles[n].getText(),
#                         "photo": product_imageDiv[n].find("img").get('data-src'),
#                         "description": "This is a product",
#                         "price": product_prices[n].getText().strip(),
#                         "compare_price": 0.01,
#                         "category": category,
#                         "quantity": 0,
#                         "sold": "N/A",
#                         # "date_created": date.today().strftime("%Y-%m-%d"),
#                         "date_created": '2022-12-10',
#                         "inOffer": False,
#                         "Supermarket": "Lidl"
#                         # "date_created": "Hola"
#                         }
#                     }
#     print(total_information) 


