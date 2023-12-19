from django.db import models

class ValueYearTotal(models.Model):
    year = models.CharField(max_length=4)
    total = models.FloatField()

class ValueMonthTotal(models.Model):
    month = models.CharField(max_length=15)
    value = models.FloatField()