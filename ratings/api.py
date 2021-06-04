from ratings.models import Ratings
from ratings.serializers import RatingsSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class RatingsList(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']
    lookup_field = 'user'
