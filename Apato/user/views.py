# Generic views
from rest_framework.generics import GenericAPIView, CreateAPIView


# Responses
from rest_framework.response import Response

# Status
from rest_framework import status

# Serializers
from .serializer import UserSerializer, RegisterUserSerializer

# User
from .models import User

# Permissions
from rest_framework.permissions import AllowAny, IsAdminUser


# For Register
class RegisterUser(CreateAPIView):
    """To register new user"""

    permission_classes = [AllowAny] # Allow anyone to register

    queryset = User.objects.all() # Idk why do we need querryset for register
    serializer_class = RegisterUserSerializer # serializer has all the logic




# # For Login
# class LoginUser(GenericAPIView):
#     """Have to explectely define a post function"""
    
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)

#         if serializer.is_valid():





