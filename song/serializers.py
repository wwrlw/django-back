from rest_framework import serializers
from song.models import Song
from artist.models import Artist

class ArtistSerialaizerForSong(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields ='__all__'
        fields = ['nickname','firts_name','photo','group']

class SongSerializer(serializers.ModelSerializer):
    artists_data = ArtistSerialaizerForSong(source= 'artist', many=True)
    class Meta:
        model = Song
        # fields ='__all__'
        exclude = ['artist']
