from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.
class MyStudents(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    user_profile_pic = models.ImageField(upload_to="profiles_img")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        # ordering = ['username']
        verbose_name = "User student"

