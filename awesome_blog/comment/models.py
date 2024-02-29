from django.db import models
from django.conf import settings
from tag.models import Tag


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
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
