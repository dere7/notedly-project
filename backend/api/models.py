from django.db import models
from django.db.models.expressions import OrderBy

class Note(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    body  = models.TextField()
    likes = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createdAt']