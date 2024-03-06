from django.core.management.base import BaseCommand
from faker import Faker

from post.models import Post
from comment.models import Comment
from tag.models import Tag
from user.models import User
import random


class Command(BaseCommand):
    help = 'Create fake comments'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of comments to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        users = User.objects.all()
        posts = Post.objects.all()

        for i in range(total):
            post = random.choice(posts)
            created_by = random.choice(users)
            content = fake.text()
            comment = Comment.objects.create(
                post=post,
                created_by=created_by,
                content=content
            )

            tags = [fake.word() for _ in range(random.randint(0, 5))]
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(content=tag_name)  # Tag 모델의 필드가 name이라고 가정
                comment.tags.add(tag)  # Post 인스턴스에 tag 추가

            self.stdout.write(self.style.SUCCESS(f'{i + 1} 번째 comment 만들기 성공!'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} comments'))
