from django.urls import path
from ratings.api import RatingsList

urlpatterns = [
    path('ratings/', RatingsList.as_view())
]