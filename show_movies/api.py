from rest_framework.viewsets import ModelViewSet
from .serializers import ProfilesSerializer, MoviesSerializer, RatingsSerializer
from .models import Profiles, Movies, Ratings


class ProfilesViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


# @api_view(['GET', 'POST'])
# def profile(request):
#     if request.method == 'GET':
#         snippets = Profiles.objects.all()
#         serializer = ProfilesSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProfilesSerializer(data=request.data)4444444EATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class RatingsViewSet(ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer