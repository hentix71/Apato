from django.db import models
from django.conf import settings

# Create your models here.
class Listing(models.Model):
    # Foreign Key is user
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "Listing")

    title = models.CharField(max_length = 100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits = 10, decimal_places = 2)
    address = models.CharField(max_length = 255)

    city = models.CharField(max_length = 100)

    num_guests = models.PositiveIntegerField()
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    
    is_available = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Title : {self.title} - Owner : {self.owner}"