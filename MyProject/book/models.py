from django.db import models
from django.contrib.auth.models import User
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
    departure_status_choices = [
        ('Programado', 'Programado'),
        ('Embarcando', 'Embarcando'),
        ('Cancelado', 'Cancelado'),
        ('Taxeando', 'Taxeando'),
        ('Pronto', 'Pronto'),
        ('Autorizado', 'Autorizado'),
        ('Em voo', 'Em voo'),
        ('Pousando', 'Pousando'),
        ('Atterissado', 'Atterissado'),]
    ID = models.IntegerField(primary_key=True)
    ID_VOO = models.ForeignKey(Voo, on_delete=models.CASCADE)
    DH_REAL_SAIDA = models.DateTimeField(null=True, blank=True,auto_now=False)
    DH_REAL_CHEGADA = models.DateTimeField(null=True, blank=True,auto_now=False   )
    NM_STATUS = models.CharField(max_length=50, null=False, choices=departure_status_choices, default='Programado')
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

class Relatorio(models.Model):
    data_inicio = models.DateTimeField(null=True, blank=True,auto_now=False)
    data_fim = models.DateTimeField(null=True, blank=True,auto_now=False   )
    class Meta:
        db_table = 'Relatorio'

class User(models.Model):
  
    class Meta:
        permissions = (("access_relatorio", "can access relatorio page"),("generate_relatorio ","can generate relatorio"),("access_atualizar","can access to atualizar voo page"),)
        
