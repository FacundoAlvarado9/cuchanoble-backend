# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0006_remove_perro_encontro_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='encontro_casa',
            field=models.BooleanField(default=False),
        ),
    ]
