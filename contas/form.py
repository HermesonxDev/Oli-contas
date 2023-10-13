from django.forms import ModelForm
from .models import *

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['banco', 'tipo', 'data', 'descricao', 'valor', 'categoria', 'observacoes']