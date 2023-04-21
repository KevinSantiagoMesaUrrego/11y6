# Generated by Django 4.1.7 on 2023-04-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_rename_marca_marca_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]
