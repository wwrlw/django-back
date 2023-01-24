from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from artist.models import Artist
from artist.serializers import ArtistSerializer

@api_view()
def artist_list(request):
    artists = Artist.objects.all()
    data = ArtistSerializer(isinstance=artists, many=True).datta
    return Response(data={'data':data})
    