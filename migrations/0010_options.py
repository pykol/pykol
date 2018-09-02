# Generated by Django 2.1 on 2018-08-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pykol', '0009_supprimer_old_codestructure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='options',
        ),
        migrations.CreateModel(
            name='OptionEtudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang_option', models.PositiveSmallIntegerField()),
                ('modalite_option', models.PositiveSmallIntegerField(choices=[(1, 'obligatoire'), (2, 'facultative')])),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pykol.Classe')),
            ],
        ),
        migrations.RemoveField(
            model_name='enseignement',
            name='specialite',
        ),
        migrations.AddField(
            model_name='enseignement',
            name='modalite_option',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'obligatoire'), (2, 'facultative')], null=True),
        ),
        migrations.AddField(
            model_name='enseignement',
            name='rang_option',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='optionetudiant',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pykol.Etudiant'),
        ),
        migrations.AddField(
            model_name='optionetudiant',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pykol.Matiere'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='options',
            field=models.ManyToManyField(through='pykol.OptionEtudiant', to='pykol.Matiere'),
        ),
    ]