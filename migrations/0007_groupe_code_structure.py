# Generated by Django 2.1 on 2018-08-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0006_collesenseignement_nomenclature_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classe',
            old_name='code_structure',
            new_name='old_code_structure',
        ),
        migrations.AddField(
            model_name='groupe',
            name='code_structure',
            field=models.CharField(blank=True, max_length=20),
		),
    ]