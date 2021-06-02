from .api import profile, RatingsViewSet, MoviesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'profiles', profile)
router.register(r'ratings', RatingsViewSet)
router.register(r'films', MoviesViewSet)

urlpatterns = router.urls