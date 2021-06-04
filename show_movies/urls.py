from .api import ProfilesViewSet, MoviesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfilesViewSet)
router.register(r'films', MoviesViewSet)

urlpatterns = router.urls
