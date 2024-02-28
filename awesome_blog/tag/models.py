from django.db import models


class Tag(models.Model):
    content = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.content
