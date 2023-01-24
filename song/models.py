from django.db import models
from artist.models import Artist
from fit.models import Fit


class Song(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    
    artist = models.ManyToManyField(to=Artist, related_name='songs', verbose_name='Исполнители')

    description = models.TextField(verbose_name='Описание')
    audio_file = models.FileField(verbose_name='Аудиофайл', upload_to='songs/audios')
    cover = models.ImageField(verbose_name='Обложка', upload_to='songs/photos')
    realised_at = models.DateField(verbose_name='Выпушен', auto_now=False, auto_now_add=False)
    # number_of_voutes = models.IntegerField(verbose_name='Количество голосов')
    fit = models.ForeignKey(Fit, verbose_name='Фиты', on_delete=models.PROTECT)
    

    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
