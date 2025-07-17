from rest_framework import serializers

# Models
from .models import User

# For Basic and Listing
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_host", "bio", "profile_picture"] # This fields will be shown during listing



# For Register
class RegisterUserSerializer(serializers.ModelSerializer):
    
    """Extra field(not related to model) : For password confirnmation"""
    confirm_password = serializers.CharField(max_length = 128, write_only = True)

    class Meta:
        model = User # belongs to user model

        # Following fields are required when creating a user
        fields = [ "id", "username", "email", "password", "confirm_password", "is_host", "bio", "profile_picture"]

        # Extra meta data for password
        extra_kwargs = {
            "password": { "write_only" : True} # Only can be written
        }

        
    """Custom Validation"""
    def validate(self, attrs):
        """attrs (Dictionary ) => Consists all the fields defined in model and above"""

        errors  = {} # Dict for errors

        # For Password
        if attrs['confirm_password'] != attrs['password']:

            """A detialed way to raise password error"""
            errors['Passwrod errror'] = [
                "Password did not match",
                f"Confirm Passwrod: {attrs['confirm_password']}",
                f"Passwrod: {attrs['password']}"
            ]

            if errors:
                """If there are any erros"""
                raise serializers.ValidationError(errors)
        
        return attrs # attrs -> validated_data
    

    def create(self, validated_data):
        """Create user with validated data"""



        validated_data.pop("confirm_password")

        print(f'Validated Data: {validated_data}')
        user = User.objects.create_user(**validated_data)
        print(f"from serializer type : {type(user)}")
        print(f'User :{user.username} created')

        return user



