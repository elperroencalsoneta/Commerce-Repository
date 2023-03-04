from django.urls import path


from .views import SearchSupermarktView

app_name="supermarkt"
urlpatterns = [
    path('search-market', SearchSupermarktView.as_view()),
]