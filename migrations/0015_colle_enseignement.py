# Generated by Django 2.1 on 2018-08-24 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0014_creneau_colles_ens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colle',
            name='matiere',
        ),
        migrations.AddField(
            model_name='colle',
            name='enseignement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pykol.Enseignement'),
        ),
    ]
