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

class RelatorioFormulario(forms.ModelForm):
    relatorio = forms.CharField(label="Relatorio")
    DH_PREVISTO_CHEGADA_i = forms.DateField(label="data prevista de chegada inicial")
    DH_PREVISTO_CHEGADA_f = forms.DateField(label="data prevista de chegada final")
    
class VooFormularioUpdate(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA',
                  'NM_AEROPORTO_SAIDA', 'NM_AEROPORTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels = {"DH_PREVISTO_SAIDA": "HORÁRIO DE SAIDA PREVISTO",
                  "DH_PREVISTO_CHEGADA": "HORÁRIO DE CHEGADA PREVISTO", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA",
                  "NM_AEROPORTO_CHEGADA": "AEROPORTO CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}


CHOICES = (('pronto',"pronto"),('cancelado',"cancelado"),)

class VooRealFormularioUpdate(forms.ModelForm):
        NM_STATUS = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple, choices=CHOICES, required = True)
        DH_REAL_SAIDA =  forms.DateTimeField(required = True)
        DH_REAL_CHEGADA =  forms.DateTimeField(required = True)
        class Meta:
            model = VooReal
        
            fields = ['DH_REAL_SAIDA', 'DH_REAL_CHEGADA', 'NM_STATUS']
            labels = {"DH_REAL_SAIDA" : "HORÁRIO DE SAIDA REAL", "DH_REAL_CHEGADA" :"HORÁRIO DE CHEGADA PREVISTO" , "NM_STATUS" : "STATUS DO VOO"}