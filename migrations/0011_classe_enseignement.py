# Generated by Django 2.1 on 2018-08-27 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0010_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='enseignements',
        ),
        migrations.AddField(
            model_name='enseignement',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='enseignements', to='pykol.Classe'),
            preserve_default=False,
        ),
    ]
