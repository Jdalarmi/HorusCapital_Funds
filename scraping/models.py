from django.db import models
from django.contrib.auth.models import User

class FundsHorus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fund = models.CharField(max_length=15, null=False)
    value = models.CharField(max_length=8, null=False)
