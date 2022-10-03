from django.db import models
from django.utils.text import slugify

# Create your models here.

class Gallery (models.Model):
    title=models.CharField(max_length=512)

    class Meta:
        ordering = ('-id',)

class Photo (models.Model):
    pic=models.ImageField(upload_to='image/')
    slug=models.SlugField(max_length=200, blank=True)
    galery=models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self)
            super().save(*args, **kwargs)

class Tariff (models.Model):
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
