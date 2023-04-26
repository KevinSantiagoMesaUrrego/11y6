# Generated by Django 4.1.7 on 2023-04-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField(max_length=45, verbose_name='Cantidad Producto')),
                ('valor_total', models.FloatField(max_length=45, verbose_name='Valor Total Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=45, verbose_name='Nombre Evento')),
                ('fecha_inicio', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Incio Evento')),
                ('fecha_fin', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Fin Evento')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción Evento')),
                ('estado_evento', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_identificacion', models.CharField(choices=[('CC', 'Cédula'), ('CE', 'Cédula de Extranjería')], max_length=2, verbose_name='Tipo de Identificación')),
                ('nombre_proveedor', models.CharField(max_length=45, verbose_name='Nombre Proveedor')),
                ('apellido_proveedor', models.CharField(max_length=45, verbose_name='Apellido Proveedor')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('correo_proveedor', models.CharField(max_length=50, verbose_name='Correo Proveedor')),
                ('direccion_proveedor', models.CharField(max_length=50, verbose_name='Dirección Proveedor')),
                ('estado_proveedor', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado Proveedor')),
            ],
        ),
    ]
