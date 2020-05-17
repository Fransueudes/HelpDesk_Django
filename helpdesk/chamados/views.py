from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Chamado, Categoria
from .forms import ChamadoForm

from django.views.generic.edit import FormView
from django.views.generic import TemplateView

def inicial(request):
    chamados = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            chamados = Chamado.objects.filter()
        else:
            chamados = Chamado.objects.filter(autor__usuario=request.user)
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

    return render(request, 'chamados/inicial.html', {'chamados': chamados})


def detalhes(request, id_chamado):
    if request.user.is_authenticated:
        chamado = Chamado.objects.get(pk=id_chamado)
        return render(request, 'chamados/detalhes.html', {'chamado': chamado})
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

class ChamadoView(FormView):
    template_name = "chamados/solicita.html"
    form_class = ChamadoForm

    def form_valid(self, form):
        dados = form.clean()
        chamado = Chamado(titulo=dados['titulo'], descricao=dados['descricao'], telefone=dados['telefone'], categoria=dados['categoria'])
        chamado.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chamado_sucesso')

class ChamadoSucessoView(TemplateView):
    template_name = "chamado/chamado_sucesso.html"