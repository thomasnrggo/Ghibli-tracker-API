from django.db import models
from show_movies.models import Movies
from users.models import Profile
import uuid


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