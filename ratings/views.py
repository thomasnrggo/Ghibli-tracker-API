from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ratings.models import Ratings
from ratings.serializers import RatingsSerializer


@api_view(['GET', 'POST'])
def rating(request):

    if request.method == 'GET':
        snippets = Ratings.objects.all()
        serializer = RatingsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)