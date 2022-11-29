# Generated by Django 4.1.3 on 2022-11-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonajesApp', '0002_datospersonaje_delete_datospersonales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosfamilia',
            old_name='nombre',
            new_name='familia',
        ),
        migrations.RenameField(
            model_name='datosfamilia',
            old_name='profesion',
            new_name='profesionFamilia',
        ),
        migrations.RenameField(
            model_name='datosprofesion',
            old_name='nombre',
            new_name='profesion',
        ),
        migrations.AlterField(
            model_name='datospersonaje',
            name='raza',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='datosprofesion',
            name='renombre',
            field=models.CharField(max_length=50),
        ),
    ]
