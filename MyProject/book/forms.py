from django import forms
from .models import Voo


class VooFormulario(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['ID_VOO', 'DH_PREVISTO_SAIDA', 'DH_PREVISTO_CHEGADA',
                  'NM_AEROPORTO_SAIDA', 'NM_AEROPORTO_CHEGADA', 'NM_COMPANHIA_AEREA']
        labels = {"ID_VOO": "ID", "DH_PREVISTO_SAIDA": "HORÁRIO DE SAIDA PREVISTO",
                  "DH_PREVISTO_CHEGADA": "HORÁRIO DE CHEGADA PREVISTO", "NM_AEROPORTO_SAIDA": "AEROPORTO SAIDA",
                  "NM_AEROPORTO_CHEGADA": "AEROPORTO CHEGADA", "NM_COMPANHIA_AEREA": "COMPANHIA AEREA"}

        #widgets = {"DH_PREVISTO_SAIDA": forms.TimeInput}
