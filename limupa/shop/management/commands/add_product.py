import random
from django.core.management.base import BaseCommand
from shop.models import Product, Detailed, ProductImage, ProductCategory, Company, GeneralProductCategory
from django.utils.text import slugify
from faker import Faker
from time import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(1, 100):
            title_g = fake.text(7)
            title_c = fake.text(7)
            title_k = fake.text(10)
            title_p = fake.text(50)
            #add_generalcategory
            GeneralProductCategory.objects.create(
                title=title_g,
                slug=slugify(title_g)
            )
            # add_category
            ProductCategory.objects.create(
                title=title_c,
                slug=slugify(title_c),
                general=GeneralProductCategory.objects.all().order_by('?').first(),
            )
            # add_company
            Company.objects.create(
                title=title_k,
                slug=slugify(title_k)
            )
            # add_product
            p = Product.objects.create(
                title=title_p,
                slug=slugify(title_p),
                description=fake.text(15),
                category=ProductCategory.objects.all().order_by('?').first(),
                company=Company.objects.all().order_by('?').first()
            )
            #add_product
            image = ProductImage.objects.create(
                product_id=p,
                image='shop/zevs.jpeg',
                is_general=True
            )

            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')

