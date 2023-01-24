from django.db import models

class Fit(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    realised_at = models.DateField(verbose_name='Выпушен', auto_now=False, auto_now_add=False)
    # number_of_voutes = models.IntegerField(verbose_name='Количество голосов')
    # song
    

    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Фит'
        verbose_name_plural = 'Фиты'

