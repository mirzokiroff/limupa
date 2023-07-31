from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    # country = models.CharField(max_length=255, blank=True, null=True)
    # company_name = models.CharField(max_length=255, blank=True, null=True)
