# Generated by Django 4.1.5 on 2023-01-25 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_alter_group_description_alter_group_title'),
        ('artist', '0004_alter_artist_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='Группы'),
        ),
    ]
