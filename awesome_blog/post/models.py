from django.db import models
from django.conf import settings


class Tag(models.Model):
    content = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):  # TODO: view로 옮겨야함. comment도 마찬가지
        tags = list(self.tags.all())
        super().delete(*args, **kwargs)  # Post 인스턴스를 먼저 삭제
        for tag in tags:
            if not tag.posts.exists() and not tag.comments.exists():
                tag.delete()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='comments', blank=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.created_by, self.post)

    def delete(self, *args, **kwargs):
        tags = list(self.tags.all())
        super().delete(*args, **kwargs)  # Comment 인스턴스를 먼저 삭제
        for tag in tags:
            if not tag.posts.exists() and not tag.comments.exists():
                tag.delete()
