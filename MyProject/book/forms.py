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
    class Meta:
        model = Voo
        fields = ['DH_PREVISTO_SAIDA','DH_PREVISTO_CHEGADA','NM_AEROPORTO_SAIDA','NM_AEROPORTO_CHEGADA']

class VooFormularioUpdate(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA',
                  'NM_AEROPORTO_SAIDA', 'NM_AEROPORTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels = {"DH_PREVISTO_SAIDA": "HORÁRIO DE SAIDA PREVISTO",
                  "DH_PREVISTO_CHEGADA": "HORÁRIO DE CHEGADA PREVISTO", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA",
                  "NM_AEROPORTO_CHEGADA": "AEROPORTO CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}


departure_status_choices = [('Programado', 'Programado'),
        ('Embarcando', 'Embarcando'),
        ('Cancelado', 'Cancelado'),
        ('Taxeando', 'Taxeando'),
        ('Pronto', 'Pronto'),
        ('Autorizado', 'Autorizado'),
        ('Em voo', 'Em voo'),
        ('Pousando', 'Pousando'),
        ('Atterissado', 'Atterissado'),
    ]

class VooRealFormularioUpdate(forms.ModelForm):
      NM_STATUS = forms.ChoiceField(widget=forms.RadioSelect, choices=departure_status_choices)
      class Meta:
            model = VooReal
            fields = ['NM_STATUS']
            labels = {"NM_STATUS" : "NM_STATUS"}
            

class SearchCRUD(forms.ModelForm):
    class Meta:
        model = Voo
        fields =['ID']
        

class CompanhiaRelatorio(forms.ModelForm):
    class Meta:
        model = Voo
        fields=['DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels={"DH_PREVISTO_SAIDA": "DATA SAIDA", "DH_PREVISTO_CHEGADA": "DATA CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}

class AeroportoRelatorio(forms.ModelForm):
    class Meta:
        model = Voo
        fields=['DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA', 'NM_AEROPORTO_SAIDA']
        labels={"DH_PREVISTO_SAIDA": "DATA SAIDA", "DH_PREVISTO_CHEGADA": "DATA CHEGADA", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA"}
