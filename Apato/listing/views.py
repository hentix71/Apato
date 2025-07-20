from .serializers import CreateListingSerializer

from rest_framework.generics import CreateAPIView

from .customListingPermissions import IsHost

from .models import Listing

from rest_framework.response import Response
from rest_framework import status



# For Lisitng properties
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


