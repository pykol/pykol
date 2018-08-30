# Generated by Django 2.1 on 2018-08-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0012_representation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mefmatiere',
            name='periode',
            field=models.PositiveSmallIntegerField(choices=[(0, 'année complète'), (1, 'première période'), (2, 'deuxième période')], default=0, verbose_name='période'),
        ),
    ]
