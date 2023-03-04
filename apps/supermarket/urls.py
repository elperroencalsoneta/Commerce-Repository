from django.urls import path


from .views import search_supermarket, supermarket_website_check, scrape_offers
from . import views

app_name="supermarket"
urlpatterns = [
    path('store_locator', views.search_supermarket, name="store_locator"),
    path('website_checking', views.supermarket_website_check, name="website_checking"),
    path('scrape_offers', views.scrape_offers, name=",scrape_offers")
]