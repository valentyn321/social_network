from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return f'{self.user.username}: {self.content}'
