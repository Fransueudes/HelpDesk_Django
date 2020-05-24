from django import forms
from django.forms import ModelChoiceField
from .models import Chamado, Categoria, Status



class ChamadoForm(forms.Form):
    titulo = forms.CharField(max_length=128)
    telefone = forms.CharField(max_length=14, min_length=9)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), initial=0)
    descricao = forms.CharField(widget=forms.Textarea)
  
    def clean(self):
        dados = super().clean()
        return dados


class AtendimentoForm(forms.Form):
    chamado = forms.ModelChoiceField(queryset=Chamado.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all(), initial=0)
    descricao = forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados = super().clean()
        return dados