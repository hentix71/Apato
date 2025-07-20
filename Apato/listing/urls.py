from django.urls import path
from .views import CreateListing, DeleteListing, ListListing, UpdateListing





urlpatterns = [
    #Create Listing 
    path("create/", CreateListing.as_view(),name = "Listing new Property"),

    #Delete Listing 
    path("delete/<int:id>", DeleteListing.as_view(),name = "Delete Property"),

    # Listing 
    path("list/", ListListing.as_view(),name = "List Properties"),

    # Update Listing
    path("update/<int:id>", UpdateListing.as_view(),name = "Update Properties"),

    
]
