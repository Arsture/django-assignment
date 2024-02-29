from django.core.management.base import BaseCommand
from faker import Faker

from post.models import Post
from tag.models import Tag
from user.models import User
import random


class Command(BaseCommand):
    help = 'Create fake posts'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of posts to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        users = User.objects.all()

        for i in range(total):
            title = fake.sentence()
            description = fake.text()
            post = Post.objects.create(
                title=title,
                description=description,
                created_by=random.choice(users)
            )

            tags = [fake.word() for _ in range(random.randint(0, 5))]
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(content=tag_name)  # Tag 모델의 필드가 name이라고 가정
                post.tags.add(tag)  # Post 인스턴스에 tag 추가

            self.stdout.write(self.style.SUCCESS(f'{i + 1} 번째 post 만들기 성공!'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} posts'))
