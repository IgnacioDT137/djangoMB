# Generated by Django 4.0.4 on 2022-07-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_promo_codigo_promo_porcentaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
    ]