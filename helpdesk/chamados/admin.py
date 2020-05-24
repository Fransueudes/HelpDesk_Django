from django.contrib import admin
from .models import *


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
	readonly_field = ('date',)
@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass
