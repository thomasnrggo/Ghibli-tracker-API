from django.urls import path
from ratings.views import rating

urlpatterns = [
    path('ratings/', rating, name='Ratings')
]