#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sensorId(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    note = models.CharField(max_length=64,verbose_name="备注")

class minData(models.Model):
    PM25 = models.CharField(max_length=32)
    TVOC = models.CharField(max_length=32)
    HCOC = models.CharField(max_length=32)
    TEMP = models.CharField(max_length=32)
    WEIG = models.CharField(max_length=32)
    DATE = models.DateTimeField(auto_now=True)
    devId = models.ForeignKey(sensorId)

    def __unicode__(self):
        return self.devId_name

class HouData(models.Model):
    PM25 = models.CharField(max_length=32)
    TVOC = models.CharField(max_length=32)
    HCOC = models.CharField(max_length=32)
    TEMP = models.CharField(max_length=32)
    WEIG = models.CharField(max_length=32)
    DATE = models.DateTimeField(auto_now=True)
    devId = models.ForeignKey(sensorId)

    def __unicode__(self):
        return self.devId_name


class dayData(models.Model):
    PM25 = models.CharField(max_length=32)
    TVOC = models.CharField(max_length=32)
    HCOC = models.CharField(max_length=32)
    TEMP = models.CharField(max_length=32)
    WEIG = models.CharField(max_length=32)
    DATE = models.DateTimeField(auto_now=True)
    devId = models.ForeignKey(sensorId)

    def __unicode__(self):
        return self.devId_name

class rawDatas(models.Model):
    PM25 = models.CharField(max_length=32)
    TVOC = models.CharField(max_length=32)
    HCOC = models.CharField(max_length=32)
    TEMP = models.CharField(max_length=32)
    WEIG = models.CharField(max_length=32)