# Generic views
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

# Responses
from rest_framework.response import Response

# Status
from rest_framework import status

# Serializers
from .serializer import UserSerializer, RegisterUserSerializer, LoginUserSerializer, UpdateUserSerializer

# User
from .models import User

# Permissions
from rest_framework.permissions import AllowAny, IsAdminUser

# Pagination
from custom_pagination import CustomCursorPagination

# Permission
from .custom_permission import IsAdminOrOwner



# For Delete
class DeleteUser(DestroyAPIView):
    permission_classes = [IsAdminOrOwner]
    lookup_field = "id"
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        """The delete part is directly done using the "destroy" view. here the parmaeter '*args' and '**kwargs' is used 
        as they carries the data 'id' which is required by 'delete()' method to delete the user"""
        instance = self.get_object()

        user_email = instance.email

        instance.delete()

        return Response({
            "Message": "Delete Sucessfull",
            "User Email": user_email
        }
        )



# For Update
class UpdateUser(UpdateAPIView):
    permission_classes = [IsAdminOrOwner]
    lookup_field = "id"
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()




# For Login
class LoginUser(GenericAPIView):

    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer # required for Swagger api input fileds

    """Have to explectely define a post function"""
    def post(self, request):
        serializer = LoginUserSerializer(data = request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




# For Listing 
class ListUsers(ListAPIView):
    """To list out all registered users"""
    permission_classes = [AllowAny] # only admin can list all the registered users

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Explectly Impleting the custom pagination
    pagination_class = CustomCursorPagination




# For Register
class RegisterUser(CreateAPIView):
    """To register new user"""

    permission_classes = [AllowAny] # Allow anyone to register

    queryset = User.objects.all() # Idk why do we need querryset for register
    serializer_class = RegisterUserSerializer # serializer has all the logic

    # """For Custom response message """
    # def create(self, request, *args, **kwargs):
    #     call_serializer_create = super().create(request, *args, **kwargs)
        
    #     # gets the created user instacne
    #     user = self.get_serializer().instance

    #     print(f"From view type : {type(user)} and the user : {user}")
            
    #     success_message = {
    #         "Message": "Sucessfully User Registered"
    #     }

    #     return Response(success_message, status = status.HTTP_201_CREATED)

