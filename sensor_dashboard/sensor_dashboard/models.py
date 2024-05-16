# sensor_dashboard/models.py

from django.db import models

class SensorData(models.Model):
    mq4 = models.FloatField()
    co2 = models.FloatField()
    lidar = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UGVPosition(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
