# Generated by Django 4.0.4 on 2022-06-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=16)),
                ('apellido', models.CharField(max_length=16)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pwd', models.CharField(max_length=12)),
            ],
        ),
    ]
