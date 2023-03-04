from django.shortcuts import render
from geopy import distance
from geopy.geocoders import Nominatim
from apps.supermarkt.models import Supermarkt
from .models import Supermarkt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

class SearchSupermarktView(APIView):
    geolocator = Nominatim(user_agent="store_locator")
    location = geolocator.geocode("Marktstraße 16 76726 Germersheim")
    userLocation = (location.latitude, location.longitude)
    print(userLocation)

    def supermarkets_near_me(request):
        user_lat = request.GET.get('lat')
        user_lng = request.GET.get('lng')
        user_location = (user_lat, user_lng)

        supermarkets = Supermarkt.objects.all()
        supermarkets_near_me = []
        for supermarket in supermarkets:
            supermarket_location = (supermarket.lat, supermarket.lng)
            distanz = distance(user_location, supermarket_location).miles
            if distanz < 5:  # Only include supermarkets within 5 miles of the user
                supermarkets_near_me.append(supermarket)

        supermarkets_near_me = sorted(supermarkets_near_me, key=lambda x: x.distanz)  # Sort supermarkets by distance

        context = {'supermarkets': supermarkets_near_me}
        return render(request, 'supermarkets.html', context)