from rest_framework import serializers

from .models import Listing







# Update Serializer
class UpdateListingSerializre(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [ "title", "description", "price_per_night",
                "address", "city", "num_guests", "num_bedrooms", 
                "num_bathrooms", "is_available", "updated_at"]
        
    def validate(self, attrs):
        for key, value in attrs.items():
            if value is None:
                raise serializers.ValidationError("Enter Atleast one value")
            
        # list instance
        list_instance = self.instance

        # Errors
        errors = {}

        for i in ["title", "description", "price_per_night","address", "city", "num_guests", "num_bedrooms", 
                "num_bathrooms", "is_available", "updated_at"]:
            
            if getattr(list_instance, i) == attrs.get(i):
                errors["Enter"] = "Enter new value for atleast one"
        
        if errors:
            return serializers.ValidationError(errors)
        
        return attrs
    
    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            if value is not None:
                setattr(instance, key, value)
            
        instance.save()
        return instance






# Listing Serializer
class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "title", "description", "price_per_night",
                "address", "city", "num_guests", "num_bedrooms", 
                "num_bathrooms", "is_available", "created_at", "updated_at"]
        read_only_fields = ['created_at']


