# Generated by Django 4.1.5 on 2023-01-25 22:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0006_favouriteproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouriteProduct',
            new_name='VouteFor',
        ),
    ]
