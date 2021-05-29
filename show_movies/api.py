from rest_framework.viewsets import ModelViewSet

from .serializers import ProfilesSerializer, MoviesSerializer, RatingsSerializer
from .models import Profiles, Movies, Ratings


class ProfilesViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class RatingsViewSet(ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer