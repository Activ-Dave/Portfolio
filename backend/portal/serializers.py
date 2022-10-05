from rest_framework import serializers
from portal.models import Gallery, Photo, Tariff

class GallerySerial (serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class PhotoSerial (serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class TariffSerial (serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'
