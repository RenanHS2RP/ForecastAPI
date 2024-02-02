from django.db import models

# Create your models here.
class User(models.Model):
    temperature = models.CharField(max_length=255)
    atmosphere_pressure = models.EmailField(max_length=255)
    humidity = models.IntegerField()
    preceptation = models.
    wheather_condition
    time = models.DateTimeField()
git checkout -b main
