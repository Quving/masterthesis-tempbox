from django.db import models


# Create your models here.
class Measurement(models.Model):
    measurement_id = models.CharField(max_length=32)
    lat = models.FloatField()
    lng = models.FloatField()
    source = models.CharField(max_length=64)
    timezone = models.CharField(max_length=64)
    timestamp = models.BigIntegerField()
    temperature = models.IntegerField()
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    altitude = models.IntegerField()
