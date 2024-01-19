from django.db import models

class FundsHorus(models.Model):
    fund = models.CharField(max_length=15, null=False)
    value = models.CharField(max_length=8, null=False)
