from django.shortcuts import render
from geopy import distance
from geopy.geocoders import Nominatim
from django.db import models
from serpapi import GoogleSearch
import json
import bs4


import requests
from bs4 import BeautifulSoup

# make a GET request to the website
response = requests.get("https://www.edeka.de/eh/angebote.jsp")

# parse the HTML content of the webpage
soup = BeautifulSoup(response.content, "html.parser")

# find the elements containing the product information
products = soup.find_all("div", class_="product")

# create a list to store the product information
products_info = []

# loop through each product
for product in products:
    # extract the product name and price
    name = product.find("h3").text
    price = product.find("div", class_="price").text

    # add the product information to the list
    products_info.append({
        "name": name,
        "price": price
    })

# return the list of products as a JSON response

print(products_info)
# MarketInfo = {}

# geolocator = Nominatim(user_agent="store_locator")
# location = geolocator.geocode("Hagenende 10 22143 Hamburg")
# userLocation = (location.latitude, location.longitude)
# userLocationNLP = geolocator.reverse(f'{location.latitude}, {location.longitude}')
# userPLZ = userLocationNLP.raw['address']['postcode']
# print(userLocation)

# try:
#     userCity = userLocationNLP.raw['address']['city']
# except KeyError:
#     userCity = userLocationNLP.raw['address']['town']


# params = {
#     "engine": "google_maps",
#     "q": f"Supermarkt in der Nähe",
#     "ll": f"@{location.latitude},{location.longitude},18.1z",
#     "type": "search",
#     "api_key": "81197aa8180b6bec714b612ca15f1ac1d8bac40a78fcbc41cb2a19dc2c0a4fa1",
    
# }

# search = GoogleSearch(params)
# results = search.get_dict()
# local_results = results["local_results"]
# Structured_Information = json.dumps(local_results, indent=4)


# print(Structured_Information)

# # for n in range(1, len(local_results)):
# #     # print(local_results[n]['title'])
# #     # print(local_results[n]["open_state"])
# #     # print(local_results[n]["operating_hours"])
# #     market_location = local_results[n]["gps_coordinates"]
# #     market_coordinates = (market_location["latitude"], market_location["longitude"])
# #     distance_from_user = distance.distance(userLocation, market_coordinates).km
# #     rounded_distance = round(distance_from_user, 2)

# #     try:
# #      local_results[n]['website']
# #      website = local_results[n]["website"]
# #     except KeyError:
# #      website = "Dieser Supermarkt hat keinen registrierten Website"
# #     MarketInfo[len(MarketInfo)] = {
# #         "model": "supermarket.supermarket",
# #         "pk": len(MarketInfo),
# #         "fields": {
# #             "name": local_results[n]["title"],
# #             "photo": local_results[n]['photos_link'],
# #             "address": local_results[n]["address"],
# #             "open_state": local_results[n]['open_state'],
# #             "operating_hours": local_results[n]["operating_hours"],
# #             "website": website,
# #             "distance": rounded_distance,
# #         }
# #      }



# # SortedDict = sorted(MarketInfo.items(), key=lambda x: x[1]['fields']['distance'])
# # dictionary_list = [dictionary[1] for dictionary in SortedDict]
# # listDictionaries = json.dumps(dictionary_list, indent=4)
# # print(listDictionaries)
