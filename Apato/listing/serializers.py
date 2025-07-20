from rest_framework import serializers

from .models import Listing




# Listing Serializer
class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "title", "description", "price_per_night",
                "address", "city", "num_guests", "num_bedrooms", 
                "num_bathrooms", "is_available", "created_at", "updated_at"]
        read_only_fields = ['created_at']

