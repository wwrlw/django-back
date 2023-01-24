from django.db import models
from artist.models import Artist

class Fit(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    realised_at = models.DateField(verbose_name='Выпушен', auto_now=False, auto_now_add=False)
    # artist = models.ForeignKey(Artist, verbose_name='Песня', on_delete=models.CASCADE)
    artist = models.ManyToManyField(to=Artist, related_name='fit', verbose_name='Исполнители')
    

    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Фит'
        verbose_name_plural = 'Фиты'

