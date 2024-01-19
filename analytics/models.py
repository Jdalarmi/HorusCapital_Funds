from django.db import models
from django.contrib.auth.models import User

class JurosTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_start = models.FloatField()
    value_month = models.FloatField()
    value_rentability = models.FloatField()
    
class TableFutureFees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_investido = models.FloatField()
    juros = models.FloatField()
    total_acumulado =models.FloatField()

class InsertValuesAporte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_patrimonio = models.FloatField()
    juros_recebido = models.FloatField()
    patrimonio_total = models.FloatField()

    