# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0005_auto_20171111_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='encontro_casa',
        ),
    ]
