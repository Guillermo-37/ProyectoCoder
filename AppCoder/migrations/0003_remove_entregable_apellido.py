# Generated by Django 4.1.5 on 2023-03-03 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_comision_curso_camada_entregable_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='apellido',
        ),
    ]
