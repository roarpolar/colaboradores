from django.contrib import admin
from .models import Colaborador, Matricula

# Configuração do Django Admin para Colaborador
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nasc', 'senha')  # Inclui 'senha' para visualização
    search_fields = ('nome', 'cpf')  # Adiciona 'cpf' ao campo de busca
    readonly_fields = ('senha',)  # Torna 'senha' somente leitura para segurança
    fieldsets = (
        (None, {
            'fields': ('nome', 'cpf', 'data_nasc', 'imagem', 'senha')
        }),
    )

# Configuração do Django Admin para Matricula
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'colaborador', 'funcao_atual', 'data_inicio', 'data_fim')
    list_filter = ('funcao_atual', 'data_inicio', 'data_fim')
    search_fields = ('numero', 'colaborador__nome', 'funcao_atual')
    readonly_fields = ('historico_funcoes',)  # Deixa o histórico de funções como somente leitura
    fieldsets = (
        (None, {
            'fields': ('numero', 'colaborador', 'funcao_atual', 'data_inicio', 'data_fim')
        }),
        ('Histórico', {
            'fields': ('historico_funcoes',),
        }),
    )

# Registro no Django Admin
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Matricula, MatriculaAdmin)
