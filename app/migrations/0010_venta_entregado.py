# Generated by Django 4.0.5 on 2022-07-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
    ]
