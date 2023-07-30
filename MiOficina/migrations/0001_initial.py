# Generated by Django 4.2.3 on 2023-07-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=120)),
                ('dni', models.CharField(max_length=32)),
                ('nobre_dueñor', models.CharField(max_length=64)),
                ('apellido_dueño', models.IntegerField()),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_inicio_contrato', models.DateTimeField(auto_now_add=True)),
                ('description_empresa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('cardo_asignado', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='jefeempresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nobre_jefe', models.CharField(max_length=120)),
                ('apellido_jefe', models.CharField(max_length=120)),
                ('cc_jefe', models.CharField(max_length=32)),
                ('profesion', models.CharField(max_length=120)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
