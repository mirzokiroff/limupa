from django.db import models


class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/images/', blank=True, null=True)
