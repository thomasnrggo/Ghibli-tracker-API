from django.db import models
import uuid


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
    poster_url = models.URLField()
    wiki_url = models.URLField()

    def __str__(self):
        return self.title