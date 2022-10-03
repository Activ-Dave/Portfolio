from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.is_active=True
        user.save()
        return user

    def createi_superuser(self, email, password, **kwargs):
        return self.create_user(email, password, is_superuser=True, **kwargs)

class User(AbstractBaseUser):
    email = models.EmailField('Email: ', unique=True)
    nickname = models.CharField('Nick: ', max_length=128)
    is_active = models.BooleanField('Aktywny: ', default=False)
    is_superuser = models.BooleanField('Admin: ', default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()
