from song.serializers import SongSerializer
from song.models import Song
from rest_framework.viewsets import ModelViewSet

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer