from django.urls import path
from artist.views import artist_list

urlpatterns = [
    path('artists', artist_list)
]
