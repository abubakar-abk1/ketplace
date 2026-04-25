from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Listing, ListingImage
from .serializers import ListingSerializer, ListingImageSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import ListingFilter


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = ListingFilter

    search_fields = ['title', 'description']

    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ListingImageViewSet(ModelViewSet):
    queryset = ListingImage.objects.all()
    serializer_class = ListingImageSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ListingImage.objects.filter(listing__seller = self.request.user)
