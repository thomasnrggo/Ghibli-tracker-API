from ratings.models import Ratings
from ratings.serializers import RatingsSerializer
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend


class RatingsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']
    lookup_field = 'user'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
