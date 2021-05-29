from django.urls import path
from .views import get_movies, get_ratings, profile

urlpatterns = [
    path('films/', get_movies, name='films'),
    path('ratings/', get_ratings, name='ratings'),
    path('profiles/', profile, name='profiles'),
]