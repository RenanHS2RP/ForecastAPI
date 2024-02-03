from django.db import models

# Create your models here.
class Forecast(models.Model):
    temperature = models.FloatField()
    atmosphere_pressure = models.FloatField()
    humidity = models.IntegerField()
    preceptation = models.FloatField()
    wheather_condition = models.TextChoices("ea", "eaae")
    time = models.DateTimeField()