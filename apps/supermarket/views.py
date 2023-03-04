from django.shortcuts import render
from geopy import distance
from geopy.geocoders import Nominatim
from apps.supermarket.models import Supermarket
from .models import Supermarket
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import render
from geopy import distance
from geopy.geocoders import Nominatim
from django.db import models
from serpapi import GoogleSearch
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.point import Point
from bs4 import BeautifulSoup
import spacy
import requests
import re
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}


# APLICAR ESTE TUTORIAL CUANDO EL SITIO WEB ESTE LISTO
# https://www.youtube.com/watch?v=5puz9Mb2d_c
# https://2captcha.com/demo/recaptcha-v2
# https://github.com/2captcha/2captcha-python
firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))

# load the German model for spaCy
nlp = spacy.load("de_core_news_sm")


# (53.6084282, 10.176347779048696)

@csrf_exempt  
def search_supermarket(request):
    # permission_classes = (permissions.AllowAny, )
    MarketInfo = {}

    if request.method == "POST":
            data = json.loads(request.body)
            latitude = data['latitude']
            longitude = data['longitude']
            
          

            geolocator = Nominatim(user_agent="store_locator")
            # location = geolocator.geocode("Hagenende 15 22143 Hamburg")
            userLocation = (latitude, longitude)
            pointLocation = Point(latitude, longitude)
            userLocationNLP = geolocator.reverse(pointLocation)

            userPLZ = userLocationNLP.raw['address']['postcode']
            try:
                userCity = userLocationNLP.raw['address']['city']
            except KeyError:
                userCity = userLocationNLP.raw['address']['town']

            params = {
                "engine": "google_maps",
                "q": f"Supermarkt in der Nähe",
                "ll": f"@{latitude},{longitude},21z",
                "type": "search",
                "api_key": "81197aa8180b6bec714b612ca15f1ac1d8bac40a78fcbc41cb2a19dc2c0a4fa1",
                # "hl": "de"
                
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            try:
             local_results = results["local_results"]
            except KeyError:
             return JsonResponse({"error": "No local results found"})
            Structured_Information = json.dumps(local_results, indent=4)

           

            for n in range(1, len(local_results)):

                market_location = local_results[n]["gps_coordinates"]
                market_coordinates = (market_location["latitude"], market_location["longitude"])
                distance_from_user = distance.distance(userLocation, market_coordinates).km
                rounded_distance = round(distance_from_user, 2)
                try: 
                    local_results[n]['open_state']
                    local_results[n]["operating_hours"]
                    open_state = local_results[n]['open_state']
                    operating_hours = local_results[n]["operating_hours"]
                except KeyError:
                    open_state = "Cant Determine "
                    operating_hours = "Cant Determine"
                try:
                    local_results[n]['website']
                    website = local_results[n]["website"]
                except KeyError:
                    website = "Dieser Supermarkt hat keinen registrierten Website"
                MarketInfo[len(MarketInfo)] = {
                    "model": "supermarket.supermarket",
                    "pk": len(MarketInfo),
                    "fields": {
                        "name": local_results[n]["title"],
                        "photo": local_results[n]['photos_link'],
                        "address": local_results[n]["address"],
                        "open_state": open_state,
                        "operating_hours": operating_hours,
                        "gps_coordinates": local_results[n]["gps_coordinates"],
                        "website": website,
                        "distance": rounded_distance,
                    }
                }
            SortedDict = sorted(MarketInfo.items(), key=lambda x: x[1]['fields']['distance'])
            dictionary_list = [dictionary[1] for dictionary in SortedDict]
            return JsonResponse({"user_location": userLocationNLP.raw['address'],"stores": dictionary_list}, json_dumps_params={"indent": 4})


# REMEMBER TO ADD @crf_protect with a token to avoid hackers

@csrf_exempt
def supermarket_website_check(request):
    if request.method == "POST":
        # receive the JSON response from the previous view
        data = json.loads(request.body)
        stores = data["stores"]
        # create a list to store the results
        results = []
        # loop through each store in the list
        for store in stores:
            # create a dictionary to store the result for this store
            result = {}
            result["name"] = store["fields"]["name"]
            # check if the store has a website field
            if "website" in store["fields"]:
                # if it does, check if the value is a string
                if isinstance(store["fields"]["website"], str):
                    # if it is a string, add the URL to the result dictionary
                    result["url"] = store["fields"]["website"]
                else:
                    # if it is not a string, set the URL to an empty string
                    result["url"] = ""
            else:
                # if the store does not have a website field, set the URL to an empty string
                result["url"] = ""
            # add the result dictionary to the results list
            results.append(result)

        # return the results list as a JSON response
        return JsonResponse({"results": results})

# @csrf_exempt
def scrape_offers(request):
    if request.method == "POST":
        # receive the JSON response from the previous view
        data = json.loads(request.body)
        results = data["results"]
        # create a list to store the offers
        offers = []
        # loop through each store in the list
        for result in results:
            # make a GET request to the website
            response = requests.get(result["url"])
            # parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, "html.parser")
            # find the element containing the offers
            offers_element = soup.find(class_="offers")
            if offers_element:
                # extract the text of the offers
                store_offers = [offer.text for offer in offers_element.find_all("li")]
                # add the store offers to the list of all offers
                offers.extend(store_offers)
            else:
                # search for elements with the text "Angebote" or "offers"
                offers_elements = soup.find_all(text=re.compile(r"Angebote|offers", re.IGNORECASE))
                for element in offers_elements:
                    # extract the text from the parent element
                    store_offers = element.parent.text
                    # add the store offers to the list of all offers
                    offers.append(store_offers)
        
        # return the list of offers as a JSON response
        return JsonResponse({"offers": offers})

# # THIS VERSION WORKS AND GETS THE ELEMENT WITH THE OFFER
# @csrf_exempt
# def scrape_offers(request):
#     if request.method == "POST":
#         # receive the JSON response from the previous view
#         data = json.loads(request.body)
#         results = data["results"]
#         # create a list to store the offers
#         offers = []
# # loop through each store in the list
#         for result in results:
#     # make a GET request to the website
#             response = requests.get(result["url"])
#     # parse the HTML content of the webpage
#             soup = BeautifulSoup(response.content, "html.parser")
#     # find the element containing the offers
#             offers_element = soup.find(class_="offers")
#             if offers_element:
#         # extract the text of the offers
#                 store_offers = [offer.text for offer in offers_element.find_all("li")]
#         # add the store name and offers to the list of all offers
#                 for offer in store_offers:
#                     offers.append({"supermarket": result["name"], "offer": offer})
#             else:
#                 # search for elements with the text "Angebote" or "offers"
#                  # search for elements with the text "Angebote" or "offers"
#                 offers_elements = soup.find_all("a", text=re.compile(r"Angebote|offers", re.IGNORECASE))
#                 for element in offers_elements:
#                     # extract the text from the parent element
#                     store_offers = element.parent.text
#                     # add the store name and offers to the list of all offers
#                     offers.append({"supermarket": result["name"], "offer": store_offers})

#             # return the list of offers as a JSON response
        
#         return JsonResponse({"offers": offers})

# THIS VERSION WORKS AND GETS THE ELEMENT WITH THE OFFER
# @csrf_exempt
# def scrape_offers(request):
#     if request.method == "POST":
#         # receive the JSON response from the previous view
#         data = json.loads(request.body)
#         results = data["results"]
#         # create a list to store the offers
#         offers = []
# # loop through each store in the list
#         for result in results:
#     # make a GET request to the website
#             response = requests.get(result["url"])
#     # parse the HTML content of the webpage
#             soup = BeautifulSoup(response.content, "html.parser")
#     # find the element containing the offers
#             offers_element = soup.find(class_="offers")
#             if offers_element:
#         # extract the text of the offers
#                 store_offers = [offer.text for offer in offers_element.find_all("li")]
#         # add the store name and offers to the list of all offers
#                 for offer in store_offers:
#                     offers.append({"supermarket": result["name"], "offer": offer})
#             else:
#                 # search for elements with the text "Angebote" or "offers"
#                  # search for elements with the text "Angebote" or "offers"
#                 offers_elements = soup.find_all("a", text=re.compile(r"Angebote|offers", re.IGNORECASE))
#                 for element in offers_elements:
#                     # extract the text from the parent element
#                     store_offers = element.parent.text
#                     # add the store name and offers to the list of all offers
#                     if "jobangebote" not in store_offers.lower():
#                         # add the store name and offers to the list of all offers
#                         offers.append({"supermarket": result["name"], "offer": store_offers})

#             # return the list of offers as a JSON response
        
#         return JsonResponse({"offers": offers})

# THIS VERSION WORKS TOO
# @csrf_exempt
# def scrape_offers(request):
#     if request.method == "POST":
#         # receive the JSON response from the previous view
#         data = json.loads(request.body)
#         results = data["results"]
#         # create a list to store the offers
#         offers = []
# # loop through each store in the list
#         for result in results:
#     # make a GET request to the website using the webdriver
#             response = requests.get(result["url"])
#             driver.get(result["url"])
#             # wait for the page to load
#             driver.implicitly_wait(10)
#             # get the HTML content of the page
#             html = driver.page_source
#             # parse the HTML content
#             soup = BeautifulSoup(html, "html.parser")
#     # find the element containing the offers
#             offers_element = soup.find(class_="offers")
#             if offers_element:
#         # extract the text of the offers
#                 store_offers = [offer.text for offer in offers_element.find_all("li")]
#         # add the store name and offers to the list of all offers
#                 for offer in store_offers:
#                     offers.append({"supermarket": result["name"], "offer": offer})
#             else:
#                 # search for elements with the text "Angebote" or "offers"
#                  # search for elements with the text "Angebote" or "offers"
#                 offers_elements = soup.find_all("a", text=re.compile(r"Angebote|offers", re.IGNORECASE))
#                 for element in offers_elements:
#                     # extract the text from the parent element
#                     store_offers = element.parent.text
#                     # add the store name and offers to the list of all offers
#                     if "jobangebote" not in store_offers.lower():
#                         # add the store name and offers to the list of all offers
#                         offers.append({"supermarket": result["name"], "offer Element": store_offers})

#             # return the list of offers as a JSON response
        
#         return JsonResponse({"offers": offers})

# @csrf_exempt
# def scrape_offers(request):
#     counter = 0
#     if request.method == "POST":
#         # receive the JSON response from the previous view
#         data = json.loads(request.body)
#         results = data["results"]
#         # create a list to store the offers
#         offers = []
# # loop through each store in the list
#         for result in results:
#     # make a GET request to the website using the webdriver

#             driver.get(result["url"])
#             a = ActionChains(driver)
#             # wait for the page to load
#             # driver.implicitly_wait(10)
#             time.sleep(3)
#             # print(result["url"])
#             # response = requests.get(result["url"])
#             # soup = BeautifulSoup(response.content, "html.parser")
#     # find the element containing the offers
     
#                 # search for elements with the text "Angebote" or "offers"
#                  # search for elements with the text "Angebote" or "offers"
#             # offers_elements = soup.find_all(["a", "span", "button"], text=re.compile(r"Angebote|Erlauben", re.IGNORECASE))
            
#             offers_elements = driver.find_elements(By.XPATH, "//button[contains(text(), 'Erlauben')]|//button[contains(text(), 'Zustimmen')]|//button[contains(text(), 'Akzeptieren')]|//button[contains(text(), 'Annehmem')]|//button[contains(text(), 'Zulassen')]|//button[contains(text(), 'zulassen')]|//button[contains(text(), 'akzeptieren')]|//button[contains(text(), 'bestätigen')]|//button[contains(text(), 'zustimmen')]|//button[contains(text(), 'ablehnen')]|//button[contains(text(), 'OK')]")
#             for element in offers_elements:
#                     a.move_to_element(element).click()
#                     print("the button has been clicked")
                    
#                     driver.back()

#                     store_offers = element.parent.text

#                     # # extract the text from the parent element

#                     # if element:
#                     #     children = element.find_all()
#                     #     if children:
#                     #         for child in children:
#                     #             print(child.text)
#                     #             print(result["url"])
#                     # parent = element.prettify()
                    
#                     # element_tree = etree.fromstring(parent)
#                     # xpath = element_tree.get("class")
#                     # store_offers = element.parent.text 
#                     # print("The element was clicked")
#                     # counter += 1
#                     # time.sleep(1)
#                     # driver.back()
#                     # Construct the XPath expression

#                     # Use the element's xpath() method to find the element
#                     # result = element.xpath(xpath)
#                     # add the store name and offers to the list of all offers
#                     if store_offers is not None:
#                         if "jobangebote" not in store_offers.lower():
#                             # add the store name and offers to the list of all offers
#                             offers.append({"supermarket": result["name"], "offer Element": element})

#             # return the list of offers as a JSON response
        
#         return JsonResponse({"offers": offers})
