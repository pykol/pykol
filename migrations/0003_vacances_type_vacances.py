# Generated by Django 2.1 on 2018-08-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0002_creneau_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacances',
            name='type_vacances',
            field=models.PositiveSmallIntegerField(choices=[(1, 'vacances'), (2, 'férié')], default=1),
        ),
    ]
