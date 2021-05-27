from django.urls import path
from .views import profile

urlpatterns = [
    path('profiles/', profile, name='profiles'),
]