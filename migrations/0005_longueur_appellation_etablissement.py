# Generated by Django 2.1 on 2018-08-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0004_academie_id_explicite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='appellation',
            field=models.CharField(max_length=200),
        ),
    ]
