from django.db import models

# Create your models here.

class Schedule(models.Model):
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    day_of_the_week = models.IntegerField(max_length=20, null=False)

