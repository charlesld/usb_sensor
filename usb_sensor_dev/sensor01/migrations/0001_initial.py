# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.CharField(max_length=32)),
                ('TVOC', models.CharField(max_length=32)),
                ('HCOC', models.CharField(max_length=32)),
                ('TEMP', models.CharField(max_length=32)),
                ('WEIG', models.CharField(max_length=32)),
                ('DATE', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.CharField(max_length=32)),
                ('TVOC', models.CharField(max_length=32)),
                ('HCOC', models.CharField(max_length=32)),
                ('TEMP', models.CharField(max_length=32)),
                ('WEIG', models.CharField(max_length=32)),
                ('DATE', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='minData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PM25', models.CharField(max_length=32)),
                ('TVOC', models.CharField(max_length=32)),
                ('HCOC', models.CharField(max_length=32)),
                ('TEMP', models.CharField(max_length=32)),
                ('WEIG', models.CharField(max_length=32)),
                ('DATE', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='sensorId',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('note', models.CharField(max_length=64, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.AddField(
            model_name='mindata',
            name='devId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor01.sensorId'),
        ),
        migrations.AddField(
            model_name='houdata',
            name='devId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor01.sensorId'),
        ),
        migrations.AddField(
            model_name='daydata',
            name='devId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor01.sensorId'),
        ),
    ]
