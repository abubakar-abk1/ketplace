from rest_framework import serializers
from .models import Listing, ListingImage


class ListingSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source='seller.username', read_only= True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['seller']

    def get_images(self, obj):
        request = self.context.get('request')
        return [
            request.build_absolute_uri(img.image.url)
            for img in obj.images.all()
        ]
    
class ListingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListingImage
        fields = ['listing', 'image', 'id']

