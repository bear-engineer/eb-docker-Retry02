from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    pass

class User(AbstractUser):
    profile_img = models.ImageField(upload_to='profile')
    objects = UserManager()

    def __str__(self):
        return self.username
