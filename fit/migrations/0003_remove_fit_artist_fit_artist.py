# Generated by Django 4.1.5 on 2023-01-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_artist_group'),
        ('fit', '0002_fit_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fit',
            name='artist',
        ),
        migrations.AddField(
            model_name='fit',
            name='artist',
            field=models.ManyToManyField(related_name='fit', to='artist.artist', verbose_name='Исполнители'),
        ),
    ]
