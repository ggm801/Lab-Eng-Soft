from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
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
    def clean(self) :
        if self.DH_PREVISTO_SAIDA > self.DH_PREVISTO_CHEGADA :
            raise ValidationError('Start date cannot precede end date')
    
    def __str__(self):
        return str(self.DH_PREVISTO_SAIDA)


    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    


class VooReal(models.Model):
    ID = models.IntegerField(primary_key=True)
    ID_VOO = models.ForeignKey(Voo, on_delete=models.CASCADE)
    DH_REAL_SAIDA = models.DateTimeField(null=True, blank=True,auto_now=False)
    DH_REAL_CHEGADA = models.DateTimeField(null=True, blank=True,auto_now=False   )
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

class User(models.Model):
  
    class Meta:
        permissions = (("view_voo_atual", "can view voo atual"),("access_relatorio", "can access relatorio page"),("generate_relatorio ","can generate relatorio"),("access_atualizar","can access to atualizar voo page"),("edit_atual", "can edit oo real"),)
        
