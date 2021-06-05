from django.urls import path
from ratings.api import RatingsList, RatingsUpdateDelete

urlpatterns = [
    path('ratings/', RatingsList.as_view()),
    path('ratings/<str:pk>/', RatingsUpdateDelete.as_view()),
]
