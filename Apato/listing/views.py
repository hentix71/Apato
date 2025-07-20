from .serializers import CreateListingSerializer, UpdateListingSerializre

from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView

from .customListingPermissions import IsHost, IsOwner

from rest_framework.permissions import AllowAny

from .models import Listing

from rest_framework.response import Response
from rest_framework import status

from custom_pagination import CustomCursorPagination




# For Update
class UpdateListing(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = UpdateListingSerializre
    queryset = Listing.objects.all()
    permission_classes = [IsOwner]




# For List
class ListListing(ListAPIView):
    serializer_class = CreateListingSerializer
    queryset = Listing.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CustomCursorPagination




# For Deleting Listed Properties
class DeleteListing(DestroyAPIView):
    serializer_class = CreateListingSerializer
    permission_classes = [IsOwner]
    queryset = Listing.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        listing_title = instance.title
        listing_id = instance.id

        instance.delete()

        return Response({
            "Message": "Delete Sucessfull",
            "Listing Id": listing_id,
            "listing Title": listing_title
        })



# For Creating properties
class CreateListing(CreateAPIView):
    serializer_class = CreateListingSerializer
    permission_classes = [IsHost]
    queryset = Listing.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data = request.data)

        serializer.is_valid(raise_exception = True)

        listing = serializer.save(owner = request.user)

        response = {
            "message": "Listing Sucessfull",
            "Listing Id": listing.id,
            "Listing Title": listing.title,
            "Listing Status": listing.is_available,

        }

        return Response(response, status = status.HTTP_201_CREATED)


