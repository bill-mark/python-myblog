# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('name', models.CharField(default='', max_length=50)),
                ('app_key', models.CharField(default='', max_length=100)),
                ('summary', models.CharField(default='', max_length=100)),
                ('app_type', models.IntegerField(default=1)),
                ('app_author', models.CharField(default='', max_length=30)),
                ('mob_logo', models.CharField(default='', max_length=100)),
                ('mob_status', models.IntegerField(default=1)),
                ('mob_url', models.CharField(default='', max_length=100)),
                ('status', models.IntegerField(default=1)),
                ('run_type', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': '应用',
                'verbose_name_plural': '应用',
            },
        ),
    ]
