# Generated by Django 4.1.5 on 2023-01-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_song_fit'),
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='song',
            field=models.ManyToManyField(related_name='album', to='song.song', verbose_name='Исполнители'),
        ),
    ]
