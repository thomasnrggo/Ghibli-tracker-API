# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfilesSerializer, MoviesSerializer, RatingsSerializer
from .models import Profiles, Movies, Ratings

# from rest_framework import status
# from rest_framework.response import Response


class ProfilesViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

#
# @api_view(['GET', 'POST'])
# def profile(request):
#     if request.method == 'GET':
#         snippets = Profiles.objects.all()
#         serializer = ProfilesSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProfilesSerializer(data=request.data)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.object.create_user(username=username, password=password)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class RatingsViewSet(ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer