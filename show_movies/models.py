from django.db import models
import uuid


class Profiles(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    username = models.CharField(max_length=32)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    password = models.CharField(max_length=64, blank=True)
    avatar_url = models.URLField(blank=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.username}"


class Movies(models.Model):
    """Movies model.

    The list of all Ghibli Studio movies along with their information.
    """

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    original_title = models.CharField(max_length=64)
    original_title_romanised = models.CharField(max_length=64)
    description = models.TextField()
    director = models.CharField(max_length=64)
    producer = models.CharField(max_length=255)
    release_date = models.IntegerField()
    running_time = models.IntegerField()
    rt_score = models.IntegerField()
    music = models.CharField(max_length=64)
    cover_url = models.URLField()
    wiki_url = models.URLField()
    thumbnail = models.URLField(blank=True)

    def __str__(self):
        return self.title