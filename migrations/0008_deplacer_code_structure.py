# Generated by Django 2.1 on 2018-08-27 05:42

from django.db import migrations

def recopier_codes_classes(apps, schema_editor):
	Classe = apps.get_model('pykol', 'Classe')
	for classe in Classe.all_objects.all():
		classe.code_structure = classe.old_code_structure
		classe.save()

def definir_codes_groupes(apps, schema_editor):
	Groupe = apps.get_model('pykol', 'Groupe')
	for groupe in Groupe.objects.filter(classe__isnull=True):
		groupe.code_structure = groupe.nom
		groupe.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0007_groupe_code_structure'),
    ]

    operations = [
			migrations.RunPython(recopier_codes_classes, elidable=True),
			migrations.RunPython(definir_codes_groupes, elidable=True),
    ]
