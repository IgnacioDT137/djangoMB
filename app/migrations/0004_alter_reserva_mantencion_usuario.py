# Generated by Django 4.0.5 on 2022-06-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_reserva_mantencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva_mantencion',
            name='usuario',
            field=models.EmailField(max_length=254),
        ),
    ]