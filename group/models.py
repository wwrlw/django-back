from django.db import models

class Group(models.Model):
    title = models.TextField(verbose_name='Название')
    description = models.CharField(verbose_name='Описание', max_length=255)
    cover = models.ImageField(verbose_name='Обложка', upload_to='groups/photos')
    created_at = models.DateField(verbose_name='Создана в:')


    def __str__ (self):
        return self.title


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
