import random
from django.core.management.base import BaseCommand
from limupa.blog.models import Post
from random import choice
from django.utils.text import slugify
from faker import Faker


class Command(BaseCommand):
    faker = Faker()

    def handle(self, *args, **options):
        post_all = Post.objects.all()

        for _ in range(1000):
            title = self.faker.sentence(6)
            product = Post.objects.create(
                title=title,
                slug=slugify(title),
                description=self.faker.text()
            )
            details = Detailed.objects.create(
                price=random.randint(200, 10000),
                quantity=random.randint(1, 1000),
                detail=random.shuffle([15.3, 14.0, 12.0, 16.0]),
                color=random.shuffle(Detailed.ProductColor.values),
                size=random.shuffle(Detailed.SizeChoices.values)
            )
            product_image = ProductImage.objects.create(
                is_general=True,
                image='zbad5tfbbe5newoz03dw.jpeg'
            )
            for i in range(3):
                product_image = ProductImage.objects.create(
                    image='2-laptop-and-monitor.jpg'
                )
            product.categories.set([choice(product_all) for _ in range(3)])
            product.company.set([choice(product_all) for _ in range(3)])
