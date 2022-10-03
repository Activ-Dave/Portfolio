from rest_framework.viewsets import ModelViewSet
from portal.models import  Gallery, Photo, Tariff, Contact, WhoIAm
from portal.serializers import GallerySerial, PhotoSerial, TariffSerial, ContactSerial, WhoIAmSerial

class GalleryVS(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerial

class PhotoVS(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerial

class TariffVS(ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerial

class ContactVS(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerial

class WhoIAmVS(ModelViewSet):
    queryset = WhoIAm.objects.all()
    serializer_class = WhoIAmSerial

