from django.db import models
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    
    artist = models.ManyToManyField(to=Artist, related_name='songs', verbose_name='Исполнители')

    description = models.TextField(verbose_name='Описание')
    audio_file = models.FileField(verbose_name='Аудиофайл', upload_to='songs/audio')
    cover = models.ImageField(verbose_name='Обложка', upload_to='artist/photos')
    realised_at = models.DateField(verbose_name='Выпушен', auto_now=False, auto_now_add=False)
    

    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
