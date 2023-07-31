from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField('shop.ProductCategory', related_name='post')
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
