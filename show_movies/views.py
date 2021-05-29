from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies, Ratings
from .serializers import MovieSerializer, RatingsSerializer
from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET', 'POST'])
def profile(request):
    if request.method == 'GET':
        snippets = Profile.objects.all()
        serializer = ProfileSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_movies(request):

    if request.method == 'GET':
        snippets = Movies.objects.all()
        serializer = MovieSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_ratings(request):

    if request.method == 'GET':
        snippets = Ratings.objects.all()
        serializer = RatingsSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)