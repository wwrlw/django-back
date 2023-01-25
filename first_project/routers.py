from rest_framework.routers import DefaultRouter
from artist.views import ArtistViewSet
from album.views import AlbumViewSet
from fit.views import FitViewSet
from group.views import GroupViewSet
from song.views import SongViewSet

router = DefaultRouter()

router.register('artists', ArtistViewSet)
router.register('album', AlbumViewSet)
router.register('fit', FitViewSet)
router.register('group', GroupViewSet)
router.register('song', SongViewSet)
