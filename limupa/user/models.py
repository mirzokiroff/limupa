from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])
    # country = models.CharField(max_length=255, blank=True, null=True)
    # company_name = models.CharField(max_length=255, blank=True, null=True)
