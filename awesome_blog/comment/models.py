from django.db import models
from django.conf import settings


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    is_updated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # 새로운 객체 생성 시에는 is_updated가 False
            self.is_updated = False
        else:
            self.is_updated = True
        super().save(*args, **kwargs)
