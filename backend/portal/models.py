from django.db import models

# Create your models here.

class Galery (models.Model):
    title=models.CharField(max_length=512)

class Photo (models.Model):
    pic=models.ImageField()
    galery=models.ForeignKey('Galery', on_delete=models.CASCADE)

class tariff (models.Model):
    name=models.CharField(max_length=512)
    time=models.CharField(max_length=128)
    much=models.IntegerField()
    price=models.IntegerField()

class Contact (models.Model):
    mail=models.EmailField(max_length=256)
    phone=models.IntegerField()
    #adress=models.CharField(max_length=1024)

class WhoIAm (models.Model):
    text=models.CharField(max_length=4096)
