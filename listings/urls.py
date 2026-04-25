from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, ListingImageViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'images', ListingImageViewSet)

urlpatterns = router.urls
