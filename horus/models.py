from django.db import models
from django.contrib.auth.models import User

class ValueYearTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    total = models.FloatField()

class ValueMonthTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=15)
    value = models.FloatField()