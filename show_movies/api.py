from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfilesSerializer, MoviesSerializer
from .models import Profiles, Movies


class ProfilesViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer