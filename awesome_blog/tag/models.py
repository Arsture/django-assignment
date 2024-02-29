from django.db import models


class Tag(models.Model):
    content = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.content
