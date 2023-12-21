from django.db import models

class JurosTable(models.Model):
    value_start = models.FloatField()
    value_month = models.FloatField()
    value_rentability = models.FloatField()
    
