# Generated by Django 4.1.7 on 2023-04-27 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={},
        ),
        migrations.AddField(
            model_name='venta',
            name='detalle_venta_cantidad_producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='venta.detalle_venta', verbose_name='detalle venta cantidad producto'),
            preserve_default=False,
        ),
    ]
