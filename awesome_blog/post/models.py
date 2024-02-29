from django.db import models
from django.conf import settings
from tag.models import Tag


class Post(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        tags = list(self.tags.all())
        super().delete(*args, **kwargs)  # Post 인스턴스를 먼저 삭제
        for tag in tags:
            if not tag.posts.exists() and not tag.comments.exists():
                tag.delete()
