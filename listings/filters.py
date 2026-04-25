import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = Listing
        fields = {
            'city': ['iexact','icontains'],
            'category':[], 
            'price': ['lt', 'gt', 'range']
        }