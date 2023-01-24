from django.http import JsonResponse
from artist.models import Artist

def artist_list(request):
    artists = Artist.objects.all()
    print(artists)
    return JsonResponse(data={'status':'ok'})
    