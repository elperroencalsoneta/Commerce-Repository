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
from django.http import JsonResponse

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}




total_information = {}
# response = requests.get("https://www.aldi-sued.de/de/angebote/d.24-11-2022.html", headers=headers)
# response = requests.get("https://www.aldi-sued.de/de/angebote/d.25-11-2022.html", headers=headers)
# data = BeautifulSoup(response.text, "html.parser")

offers_response_list = ["https://www.aldi-sued.de/de/angebote/d.22-12-2022.html", "https://www.aldi-sued.de/de/angebote/d.19-12-2022.html", 
                        "https://www.aldi-sued.de/de/angebote/d.17-12-2022.html", "https://www.aldi-sued.de/de/angebote/d.15-12-2022.html",
                        "https://www.aldi-sued.de/de/angebote/d.12-12-2022.html", "https://www.aldi-sued.de/de/angebote/d.10-12-2022.html"                    
                        ]

product_sortiment_list = ["https://www.aldi-sued.de/de/produkte/produktsortiment/neu-im-sortiment.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/kuehlung-und-tiefkuehlkost.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/nahrungsmittel.html", 
                          "https://www.aldi-sued.de/de/produkte/produktsortiment/brot-aufstrich-und-cerealien.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/kaffee-und-tee.html",
                          "https://www.aldi-sued.de/de/produkte/produktsortiment/getraenke/wein-und-sekt.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/getraenke.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/suessigkeiten-und-snacks.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/drogerie-und-kosmetik.html",
                          "https://www.aldi-sued.de/de/produkte/produktsortiment/baby-und-kind.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/haushalt.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/tierbedarf.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/blumen.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/grillen.html"
                        ]

product_welten = ["https://www.aldi-sued.de/de/produkte/produktsortiment/blumen.html", "https://www.aldi-sued.de/de/produkte/produktsortiment/grillen.html", "https://www.aldi-sued.de/de/produkte/produktwelten/einrichtung-und-wohnen.html", 
                  "https://www.aldi-sued.de/de/produkte/produktwelten/garten-und-heimwerken.html", "https://www.aldi-sued.de/de/produkte/produktwelten/technik-und-elektronik.html", "https://www.aldi-sued.de/de/produkte/produktwelten/freizeit-und-outdoor.html", 
                  "https://www.aldi-sued.de/de/produkte/produktwelten/kleidung.html"]




def scrape_aldi():
    for sortiment_response in product_sortiment_list:
        firefox_options = Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))
        driver.get(sortiment_response)
        a = ActionChains(driver)
        time.sleep(2)
        cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/form/div[3]/div/div[1]/button')
        cookies.click()
        response = requests.get(sortiment_response)
        data = BeautifulSoup(response.text, "html.parser")
        product_titles = data.findAll(name="h2", class_="product-title")
        product_prices = data.findAll(name="span", class_="price")
        product_image =  data.findAll("img", class_="at-product-images_img")
        product_category = data.find("h1", class_="plp_title")
        category = product_category
        counter = 0

        if category is not None:
                category = category.get_text()
                # print(category)
        else:
                category = "Unknown"

        # while driver.find_element(By.XPATH, '//*[@id="showMore"]') != False:
        #     showMore = driver.find_element(By.XPATH, '//*[@id="showMore"]')
        #     showMore.click()
        #     if showMore == False:
        #         break
        try:
            while driver.find_element(By.XPATH, '//*[@id="showMore"]'):
                driver.find_element(By.XPATH, '//*[@id="showMore"]').click()
                
                for n in range (len(product_prices) - 1):
                    total_information[len(total_information) + n] = {
                            "model": "product.product",
                            "pk": len(total_information) +  n,
                            "fields":
                        {
                            "name": product_titles[n].getText(),
                            "photo": product_image[n]['data-src'],
                            "description": "This is a product",
                            "price": product_prices[n].getText().strip(),
                            "compare_price": 0.01,
                            "category": category,
                            "quantity": 0,
                            "sold": "N/A",
                            # "date_created": date.today().strftime("%Y-%m-%d"),
                            "date_created": '2022-12-10',
                            "inOffer": False
                            # "date_created": "Hola"
                            }
                        }
            
        except (NoSuchElementException, ElementNotInteractableException):
            print("This Element does not exist")
            for n in range (len(product_prices) - 1):
                total_information[len(total_information) + n] = {
                            "model": "product.product",
                            "pk": len(total_information) +  n,
                            "fields":
                        {
                            "name": product_titles[n].getText(),
                            "photo": product_image[n]['data-src'],
                            "description": "This is a product",
                            "price": product_prices[n].getText().strip(),
                            "compare_price": 0.01,
                            "category": category,
                            "quantity": 0,
                            "sold": "N/A",
                            # "date_created": date.today().strftime("%Y-%m-%d"),
                            "date_created": '2022-12-10',
                            "inOffer": False
                            # "date_created": "Hola"
                            }
                        }

    for sortiment_response in product_welten:
        firefox_options = Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))
        driver.get(sortiment_response)
        a = ActionChains(driver)
        time.sleep(2)
        cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/form/div[3]/div/div[1]/button')
        cookies.click()
        response = requests.get(sortiment_response)
        data = BeautifulSoup(response.text, "html.parser")
        product_titles = data.findAll(name="h2", class_="product-title")
        product_prices = data.findAll(name="span", class_="price")
        product_image =  data.findAll("img", class_="at-product-images_img")
        product_category = data.find("h1", class_="plp_title")
        category = product_category
        counter = 0

        if category is not None:
                category = category.get_text()
                # print(category)
        else:
                category = "Unknown"

        try:
            while driver.find_element(By.XPATH, '//*[@id="showMore"]'):
                driver.find_element(By.XPATH, '//*[@id="showMore"]').click()
                
                for n in range (len(product_prices) - 1):
                    total_information[len(total_information) + n] = {
                            "model": "product.product",
                            "pk": len(total_information) +  n,
                            "fields":
                        {
                            "name": product_titles[n].getText(),
                            "photo": product_image[n]['data-src'],
                            "description": "This is a product",
                            "price": product_prices[n].getText().strip(),
                            "compare_price": 0.01,
                            "category": category,
                            "quantity": 0,
                            "sold": "N/A",
                            # "date_created": date.today().strftime("%Y-%m-%d"),
                            "date_created": '2022-12-10',
                            "inOffer": False,
                            "Supermarket": "Aldi Süd"
                            # "date_created": "Hola"
                            }
                        }
        
        
        except (NoSuchElementException, ElementNotInteractableException):
            print("This Element does not exist")
            for n in range (len(product_prices) - 1):
                total_information[len(total_information) + n] = {
                            "model": "product.product",
                            "pk": len(total_information) +  n,
                            "fields":
                        {
                            "name": product_titles[n].getText(),
                            "photo": product_image[n]['data-src'],
                            "description": "This is a product",
                            "price": product_prices[n].getText().strip(),
                            "compare_price": 0.01,
                            "category": category,
                            "quantity": 0,
                            "sold": "N/A",
                            # "date_created": date.today().strftime("%Y-%m-%d"),
                            "date_created": '2022-12-10',
                            "inOffer": False
                            # "date_created": "Hola"
                            }
                        }

                        
    for offer_response in offers_response_list:
        response = requests.get(offer_response)
        data = BeautifulSoup(response.text, "html.parser")
        product_titles = data.findAll(name="h2", class_="product-title")
        product_prices = data.findAll(name="span", class_="price")
        product_image = data.findAll("img", class_="at-product-images_img")
        offer_date = data.find("h1", class_="plp_title")
        date = ""     
        
        if offer_date is not None:
            offer_product_dates = search_dates(offer_date.text)
            if offer_product_dates is not None:
                for d in offer_product_dates:
                    date = d[1].isoformat()
                    print(date)
        
        for n in range (len(product_titles) - 1):
            total_information[len(total_information) + n] = {
                        "model": "product.product",
                        "pk": len(total_information) +  n,
                        "fields":
                    {
                        "name": product_titles[n].getText(),
                        "photo": product_image[n]['data-src'],
                        "description": "This is a product",
                        "price": product_prices[n].getText().strip(),
                        "compare_price": 0.01,
                        "category": 1,
                        "quantity": 0,
                        "sold": "N/A",
                        "date_created": date,
                        "inOffer": True,
                        "supermarket": "Aldi"

                        }
                    }
    dictionary_list = [dictionary[1] for dictionary in total_information]
    print(dictionary_list)
    print("END")
    return JsonResponse({"product_information": dictionary_list}, json_dumps_params={"indent": 4})


   














