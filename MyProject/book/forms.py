from django.forms import ModelForm
from .models import Voo

class VooForm(ModelForm):
   class Meta:
      model = Voo
      fields = ['ID', 'Previsto Saida', 'Previsto Chegada', 'Aeroporto Saida', 'Aeroporto Chegada', 'Companhia Aerea']

form = VooForm()