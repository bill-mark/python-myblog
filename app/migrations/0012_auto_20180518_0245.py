# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-18 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180517_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light_app',
            name='portal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portalapp_lightapp', to='app.Portal_app'),
        ),
    ]
