from django.core.management.base import BaseCommand

from post.models import Post, Comment


class Command(BaseCommand):
    help = 'delete all posts and comments'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        posts.update(is_updated=True)
        posts.delete()

        comments = Comment.objects.all()
        comments.delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted all posts and comments'))
