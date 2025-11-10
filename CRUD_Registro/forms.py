# CRUD_Registro/forms.py
from django import forms
from .models import Cargo, Departamento, Empregado

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nome']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'sigla']

class EmpregadoForm(forms.ModelForm):
    class Meta:
        model = Empregado
        fields = ['nome_completo', 'codigo', 'telefone', 'cargo', 'departamento']
