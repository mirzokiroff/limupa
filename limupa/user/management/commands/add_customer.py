from django.core.management.base import BaseCommand
from faker import Faker
from time import time

from user.models import OurTeam


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(1, 10):
            OurTeam.objects.create(
                image=fake.image_url(),
                name=fake.name(),
                job=fake.job(),
                email=fake.email(),
                facebook=fake.url(),
                twitter=fake.url(),
                linkedin=fake.url(),
                instagram=fake.url()
            )
            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')