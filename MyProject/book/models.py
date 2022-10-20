from asyncio import new_event_loop
from django.db import models
# Create your models here.


class Voo(models.Model):
    ID = models.IntegerField(primary_key=True)
    DH_PREVISTO_SAIDA = models.DateTimeField(auto_now=False)
    DH_PREVISTO_CHEGADA = models.DateTimeField(auto_now=False)
    ID_VOO = models.CharField(max_length=12, null=False)
    NM_AEROPORTO_SAIDA = models.CharField(max_length=50, null=False)
    NM_AEROPORTO_CHEGADA = models.CharField(max_length=50, null=False)
    NM_COMPANHIA_AEREA = models.CharField(max_length=50, null=False)
    class Meta:
        db_table = 'Voo'


class VooReal(models.Model):
    ID = models.IntegerField(primary_key=True)
    ID_VOO = models.ForeignKey(Voo, on_delete=models.CASCADE)
    DH_REAL_SAIDA = models.DateTimeField(auto_now=True)
    DH_REAL_CHEGADA = models.DateTimeField(auto_now=True)
    NM_STATUS = models.CharField(max_length=50, null=False)
    class Meta:
        db_table = 'VooReal'


class Usuario(models.Model):
    ID = models.IntegerField(primary_key=True)
    ID_USUARIO = models.CharField(max_length=12, null=False)
    FIRST_NAME = models.CharField(max_length=50, null=False)
    LAST_NAME = models.CharField(max_length=50, null=False)
    SENHA = models.CharField(max_length=50, null=False)
    USER_PERMISSION = models.IntegerField(null=False)
    class Meta:
        db_table = 'Usuario'
