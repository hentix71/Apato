from rest_framework import serializers

# Models
from .models import User

# Refresh Token
from rest_framework_simplejwt.tokens import RefreshToken







#For Update
class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "password", "bio", "profile_picture", "is_host"] # This fields can be updated
        
    
    def validate(self, attrs):

        """Extracting the fields from attrs. Using get as it assign None if no value found"""
        username = (attrs.get("username"))
        password = (attrs.get("password"))
        bio = (attrs.get("bio"))
        profile_picture = attrs.get("profile_picture")
        is_host = attrs.get("is_host")

        # Stripping
        for i in [username, password, bio, profile_picture, is_host]:
            if i is not None :
                if type(i)  is not bool:
                    i = i.strip()

        # Some value should be entered for update
        if all(i in["", None] for i in (username, password, bio, profile_picture, is_host)):
            """Atleast one field should have value, also "" empty string is none"""
            raise serializers.ValidationError("Atleast enter value for one field")
        
        """User Instance"""
        user_instance = self.instance # Getting the instance

        if user_instance is None:
            """Checking the user instance is none"""
            raise serializers.ValidationError("No instance found")
        
        # Empty Dict for collecting errors
        errors = {}


        for i in ["username", "password", "bio", "is_host", "profile_picture"]:
            
            if getattr(user_instance, i) == attrs.get(i):
                errors[i] = {i, f"Enter new Value for {i}"}

        if errors:
            """In case any error is found"""
            raise serializers.ValidationError(errors)

        return attrs


    # Update function
    def update(self, instance, validated_data):
        """Update the new value to instance"""
        for i,value in validated_data.items():
            if value is not None:
                setattr(instance, i, value) 
        instance.save()
        return instance
        








# For Login
class LoginUserSerializer(serializers.Serializer):
    """For Login Serializer : serializers.Serializer because we are just validating the entered credentials.
    Not storing those into database"""

    """Need to define fields"""
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128, write_only = True)

    def validate(self, attr):
        email = attr.get("email")
        password = attr.get("password")

        # For Email
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Email not registered"})

        # For Password
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")
        
        """Custom JWT Generation"""
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        """Custom response"""
        login_response = {
            "Message" : "Login Sucessful",
            "User Id" : user.id,
            "Username" : user.username,
            "Access Token" : str(access_token),
            "Refresh Token" : str(refresh_token)
        }

        return login_response






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



