# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180517_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light_app',
            name='summary',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
