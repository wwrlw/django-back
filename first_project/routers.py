from rest_framework.routers import DefaultRouter, SimpleRouter
from artist.views import ArtistViewSet

router = DefaultRouter()

router.register('artists', ArtistViewSet)