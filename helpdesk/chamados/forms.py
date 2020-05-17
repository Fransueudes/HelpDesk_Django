from django import forms

class ChamadoForm(forms.Form):
    titulo = forms.CharField(max_length=128)
    categoria = forms.CharField(max_length=128)
    telefone = forms.CharField(max_length=14, min_length=9)
    descricao = forms.CharField(widget=forms.Textarea)
  

    def clean(self):
        dados = super().clean()
        return dados
