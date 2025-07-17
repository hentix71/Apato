from django.contrib import admin
from django.urls import path

# Importing views
from .views import *



urlpatterns = [

    # For Admin
    # path('login/', LoginUser.as_view(), name = "For Login"),

    # For Register
    path('register/', RegisterUser.as_view(), name = "For Login"),

    # For Listing 
    path('listing/', ListUsers.as_view(), name = "For Listing users"),

    # For Login
    path('login/', LoginUser.as_view(), name = "For Login user"),

]
