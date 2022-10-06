from asyncio import new_event_loop
from django.db import models
import datetime
# Create your models here.


class Voo(models.Model):
    id = models.IntegerField(primary_key=True)
    previstoSaida = models.DateTimeField(auto_now=True)
    previstoChegada = models.DateTimeField(auto_now=True)
    VooId = models.CharField(max_length=12, null=False)
    localPartida = models.CharField(max_length=50, null=False)
    destino = models.CharField(max_length=50, null=False)
    aeroportoSaida = models.CharField(max_length=50, null=False)
    aeroportoChegada = models.CharField(max_length=50, null=False)
    compAerea = models.CharField(max_length=50, null=False)
    ##vooReal = models.ForeignKey(VooReal, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Voo'


class VooReal(models.Model):
    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    realSaida = models.DateTimeField(auto_now=True)
    realChegada = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50, null=False)
    class Meta:
        db_table = 'VooReal'
