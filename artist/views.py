
from artist.serializers import ArtistSerializer
from artist.models import Artist
from rest_framework.viewsets import ModelViewSet

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
