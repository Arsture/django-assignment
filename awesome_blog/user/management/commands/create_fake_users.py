from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User


class Command(BaseCommand):
    help = 'Create fake users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for i in range(total):
            email = fake.email()
            password = 'testpassword'
            User.objects.create_user(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'{i + 1} 번째 user 만들기 성공!'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} users'))
