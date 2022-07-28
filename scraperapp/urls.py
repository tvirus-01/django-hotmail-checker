from django.urls import path
from .views import scraper

urlpatterns = [
    #common urls
    path('', scraper),
]