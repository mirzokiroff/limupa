from django.contrib import admin
from .models import GeneralProductCategory, ProductCategory, Product, Company, Detailed

admin.site.register((GeneralProductCategory, ProductCategory, Product, Company, Detailed))
