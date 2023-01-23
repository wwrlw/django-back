from django.db import models

class Group(models.Model):
    title = models.TextField(verbose_name='')
    description = models.CharField(verbose_name='', max_length=255)
    cover = models.ImageField(verbose_name='', upload_to='groups/photos')
    created_at = models.DateField(verbose_name='')
    #artist
    #number_voutes

    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
