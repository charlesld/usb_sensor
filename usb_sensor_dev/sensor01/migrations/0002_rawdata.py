# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rawData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('PM25', models.CharField(max_length=32)),
                ('TVOC', models.CharField(max_length=32)),
                ('HCOC', models.CharField(max_length=32)),
                ('TEMP', models.CharField(max_length=32)),
                ('WEIG', models.CharField(max_length=32)),
            ],
        ),
    ]
