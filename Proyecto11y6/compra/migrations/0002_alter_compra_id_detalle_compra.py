# Generated by Django 4.2.3 on 2023-07-17 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_detalle_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.detalle_compra', verbose_name='Valor Compra'),
        ),
    ]