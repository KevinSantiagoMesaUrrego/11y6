# Generated by Django 4.2.4 on 2023-09-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_personalizacion_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizacion',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]