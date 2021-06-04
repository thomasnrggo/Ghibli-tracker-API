from rest_framework import serializers
from .models import Movies, Profiles


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'