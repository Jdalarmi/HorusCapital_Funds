from django.db import models

class JurosTable(models.Model):
    value_start = models.FloatField()
    value_month = models.FloatField()
    value_rentability = models.FloatField()
    
class TableFutureFees(models.Model):
    total_investido = models.FloatField()
    juros = models.FloatField()
    total_acumulado =models.FloatField()

class InsertValuesAporte(models.Model):
    valor_patrimonio = models.FloatField()
    juros_recebido = models.FloatField()
    patrimonio_total = models.FloatField()

    