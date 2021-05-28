from django.urls import path
from .views import get_movies

urlpatterns = [
    path('films/', get_movies, name='films'),
]