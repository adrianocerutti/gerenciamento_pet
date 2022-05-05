from typing import Text

from django import forms
from django.forms import DateInput, TextInput

from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'data_nascimento', 'profissao']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            )
        }
