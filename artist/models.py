from django.db import models
from group.models import Group

class Artist(models.Model):
    nickname = models.CharField(verbose_name='Ник', max_length=255)
    firts_name = models.CharField(verbose_name='Имя', max_length=255)
    second_name = models.CharField(verbose_name='Фамилия', max_length=255)
    description = models.TextField(verbose_name='Био')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(verbose_name='Фото', upload_to='artist/photos')
    group = models.ForeignKey(Group, verbose_name='Группы', on_delete=models.CASCADE, null=True)

    def __str__ (self):
        return self.nickname


    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
