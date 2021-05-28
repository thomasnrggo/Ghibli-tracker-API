from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies
from .serializers import MovieSerializer


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