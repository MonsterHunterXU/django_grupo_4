# Generated by Django 3.1.2 on 2020-10-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LavadoAutos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='insumos',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
