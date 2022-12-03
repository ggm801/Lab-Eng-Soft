from django import forms
from .models import Voo, VooReal


class VooFormulario(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['ID_VOO', 'DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA',
                  'NM_AEROPORTO_SAIDA', 'NM_AEROPORTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels = {"ID_VOO": "ID", "DH_PREVISTO_SAIDA": "HORÁRIO DE SAIDA PREVISTO",
                  "DH_PREVISTO_CHEGADA": "HORÁRIO DE CHEGADA PREVISTO", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA",
                  "NM_AEROPORTO_CHEGADA": "AEROPORTO CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}

        #widgets = {"DH_PREVISTO_SAIDA": forms.TimeInput}

#class RelatorioFormulario(forms.ModelForm):
 #       class Meta:
  #          model = Voo
   #         relatorio = forms.CharField()
    #        NOME = forms.TextInput()
     #       DH_PREVISTO_CHEGADA = forms.DateField()
      #      DH_PREVISTO_SAIDA = forms.DateField()
       #     fields = ['Typo_relatorio', 'Nome', 'DH_PREVISTO_CHEGADA', 'DH_PREVISTO_SAIDA']
        #    labels = {"Typo_relatorio" : "Typo de relatorio", "Nome" :"Nome" , "DH_PREVISTO_CHEGADA" : "HORÁRIO DE CHEGADA","DH_PREVISTO_SAIDA" : "HORÁRIO DE SAIDA"}
    
class FilterForm(forms.Form):
    data_inicio = forms.DateField(label='Data de início do relatório')
    data_fim = forms.DateField(label='Data de fim do relatório')
    

class VooFormularioUpdate(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA',
                  'NM_AEROPORTO_SAIDA', 'NM_AEROPORTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels = {"DH_PREVISTO_SAIDA": "HORÁRIO DE SAIDA PREVISTO",
                  "DH_PREVISTO_CHEGADA": "HORÁRIO DE CHEGADA PREVISTO", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA",
                  "NM_AEROPORTO_CHEGADA": "AEROPORTO CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}


CHOICES = [('pronto','pronto'),('cancelado','cancelado'),('Não iniciado','Não iniciado'),('Embarcando','Embarcando'),('Programado','Programado'),('Taxiando','Taxiando'),('Decolando','Decolando'),('Em Voo','Em Voo'),('Pousando','Pousando'),('Aterrissado','Aterrissado'),]



class VooRealFormularioUpdate(forms.ModelForm):
        NM_STATUS = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        DH_REAL_SAIDA =  forms.DateTimeField(required = False)
        DH_REAL_CHEGADA =  forms.DateTimeField(required = False)
        class Meta:
            model = VooReal
            fields = ['DH_REAL_SAIDA', 'DH_REAL_CHEGADA', 'NM_STATUS']
            labels = {"DH_REAL_SAIDA" : "HORÁRIO DE SAIDA REAL", "DH_REAL_CHEGADA" :"HORÁRIO DE CHEGADA PREVISTO" , "NM_STATUS" : "STATUS DO VOO"}