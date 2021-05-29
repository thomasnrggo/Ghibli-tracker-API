from django.db import models
import uuid
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


class Movies(models.Model):
    """Movies model.

    The list of all Ghibli Studio movies along with their information.
    """

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    original_title = models.CharField(max_length=32)
    original_title_romanised = models.CharField(max_length=32)
    description = models.TextField()
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=32)
    release_date = models.IntegerField()
    running_time = models.IntegerField()
    rt_score = models.IntegerField()
    music = models.CharField(max_length=32)
    cover_url = models.URLField()
    wiki_url = models.URLField()

    def __str__(self):
        return self.title


class Ratings(models.Model):
    """Ratings model.

    Model that refers to the rating a user has given to a certain movie, either emoji rating or star rating
    """

    class Meta:
        verbose_name_plural = 'Ratings'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emoji_rating = models.IntegerField()
    star_rating = models.IntegerField()
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"Star rating: {self.star_rating}, emoji rating: {self.emoji_rating}"