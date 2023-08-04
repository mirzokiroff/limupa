from django.core.management.base import BaseCommand
from user.models import OurTeam
from django.utils.text import slugify
from faker import Faker
# import  faker

from time import time

from django.core.files import File  # you need this somewhere

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(1, 5):
            image = 'media/user/zevs.jpeg'
            fl = File(open(image, 'rb'))
            OurTeam.objects.create(
                image=fake.image_url(),
                name=fake.name(),
                job=fake.job(),
                email=fake.email(),
                instagram=fake.url(),
                linkedin=fake.url(),
                twitter=fake.url(),
            )
            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')

# print(dir(faker.Faker()))