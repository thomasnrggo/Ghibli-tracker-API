from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=32)
    avatar_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user.username}"