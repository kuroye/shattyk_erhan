from django.db import models

# Create your models here.

class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_the_week = models.CharField(max_length=20)

