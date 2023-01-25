from album.serializers import AlbumSerializer
from album.models import Album
from rest_framework.viewsets import ModelViewSet

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer