from django.db import models

# Abstract User
from django.contrib.auth.models import AbstractUser

# Custom Manager
from .custom_manager import CustomManager

class User(AbstractUser):
    """Inherits : username, password from AbstractUser"""


    # Remainings
    is_host = models.BooleanField(default = False) # In host or normal user
    bio = models.TextField(max_length = 100, blank = True) # Short Bio on the user
    profile_picture = models.ImageField( upload_to = 'profile/', blank = True, null = True) # For user profile picture


    # Setting Email -> Using email for login
    email = models.EmailField(unique = True)

    username = models.CharField( unique = True, max_length=150)

    # Setting Email as login Credentials
    USERNAME_FIELD = "email"
    # Field required when creating user through Command line
    REQUIRED_FIELDS = ["username"] 


    # Assigning Custom manager for email based login
    objects = CustomManager()

    def __str__(self):
        """Identify through username in admin panel"""
        return self.username