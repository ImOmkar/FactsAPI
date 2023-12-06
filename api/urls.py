
from django.urls import path
from .views import *

urlpatterns = [
    path("facts/", FactsView.as_view()),
    path("scrap", scrap, name="scrap"),
    path("delete/", delete_data, name="delete_data"),
]
