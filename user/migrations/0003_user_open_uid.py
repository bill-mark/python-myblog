# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180516_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='open_uid',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
