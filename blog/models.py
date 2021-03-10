from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        'auth.user',
        on_delete = models.TextField()
    )
    body = models.TextField()

    def __str__(self):
        return self.title