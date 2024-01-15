from django.db import models

class FundsHorus(models.Model):
    fund = models.CharField(max_length=15)
