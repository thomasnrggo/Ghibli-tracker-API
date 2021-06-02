from .api import ProfilesViewSet, RatingsViewSet, MoviesViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'profiles', ProfilesViewSet)
router.register(r'ratings', RatingsViewSet)
router.register(r'films', MoviesViewSet)

urlpatterns = router.urls
