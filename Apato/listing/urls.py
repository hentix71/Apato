from django.urls import path
from .views import CreateListing





urlpatterns = [
    #Create Listing 
    path("create/", CreateListing.as_view(),name = "Listing new Property")
]
