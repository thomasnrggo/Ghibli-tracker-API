from django.urls import path
from .views import movie

urlpatterns = [
    path('movie/', movie, name='movie'),
]