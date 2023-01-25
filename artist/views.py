
from artist.serializers import ArtistSerializer
from artist.models import Artist
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class ArtistPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = ArtistPagination
