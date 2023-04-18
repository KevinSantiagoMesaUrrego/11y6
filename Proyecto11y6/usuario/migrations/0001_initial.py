# Generated by Django 4.1.7 on 2023-03-30 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre EPS:')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombres Completo:')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellidos Completos:')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula'), ('CE', 'Cédula de Extrangería')], max_length=2, verbose_name='Tipo de Documento:')),
                ('documento', models.IntegerField(max_length=10, verbose_name='Documento:')),
                ('rol', models.CharField(choices=[('E', 'Empleado'), ('A', 'Administrador')], max_length=1, verbose_name='Rol:')),
                ('direccion', models.CharField(max_length=45, verbose_name='Dirección:')),
                ('correo', models.CharField(max_length=45, verbose_name='Correo electronico:')),
                ('usuario', models.CharField(max_length=45, verbose_name='Usuario:')),
                ('contrasena', models.CharField(max_length=45, verbose_name='Contraseña:')),
                ('salario', models.CharField(max_length=45, verbose_name='Salario:')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre:')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellido:')),
                ('documento', models.IntegerField(max_length=10, verbose_name='Documento:')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('correo', models.CharField(max_length=45, verbose_name='Correo electronico:')),
                ('direccion', models.CharField(max_length=45, verbose_name='Dirección:')),
                ('usuario', models.CharField(max_length=45, verbose_name='Usuario:')),
                ('contrasena', models.CharField(max_length=45, verbose_name='Contraseña:')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Nacimiento')),
                ('fecha_salida', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Nacimiento')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
    ]