from django.urls import path
from .views import get_ratings


urlpatterns = [
    path('ratings/', get_ratings, name='ratings'),
]