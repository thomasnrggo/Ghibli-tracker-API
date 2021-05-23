from django.urls import path
from .views import movies

urlpatterns = [
    path('api/movies/', movies, name='movies'),
]