from django.core.management.base import BaseCommand
from fuse_blog.models import Post, Category
from random import choice
from django.utils.text import slugify
from faker import Faker
import os

from root.settings import BASE_DIR


class Command(BaseCommand):
    faker = Faker()

    def handle(self, *args, **options):
        with open('/home/user/Downloads/datas.txt', 'r') as f:
            content = f.read()
        c = Category.objects.all()
        for _ in range(1000):
            title = self.faker.sentence(6)
            p = Post.objects.create(
                main_photo='post/download.jpeg',
                title=title,
                description=self.faker.text(),
                content=content,
                publish=True,
                slug=slugify(title),
            )
            p.categories.set([choice(c) for _ in range(3)])