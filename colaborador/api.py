from ninja import Router 
from ninja import ModelSchema, Schema 
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.http import JsonResponse  
from .models import Colaborador, Matricula
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt 
from typing import List
import requests

colaborador_router = Router()
matricula_router = Router()


class ColaboradorSchema(ModelSchema):
    class Meta:
        model = Colaborador
        fields = '__all__'
   

class MatriculaSchema(ModelSchema):
    class Meta:
        model = Matricula
        fields = '__all__'

@colaborador_router.post('/colaborador/')
def add_colaborador(request, colaborador: ColaboradorSchema):
    colaborador = Colaborador(
        nome=colaborador.nome,
        senha=colaborador.senha,
        categoria_id=colaborador.matricula
    )
    colaborador.save()

    return 

# Criar uma lista de colaboradores se for necessário 
@colaborador_router.get('/colaborador/', response=List[ColaboradorSchema])
def get_colaborador(request, nome: str = None):
    colaborador_list = Colaborador.objects.all()

    if nome:
        colaborador_list = colaborador_list.filter(nome__icontains=nome)

    return colaborador_list

@matricula_router.get('/matricula/', response=List[MatriculaSchema])
def get_matricula(request):
    matricula = Matricula.objects.all()
    return matricula



################################################### VERIFICAR UMA ROTA PARA ESSE LOGIN ################################################ 


#@csrf_exempt  # Desativa CSRF para esta rota
@colaborador_router.post("/login/")
def colaborador_login_view(request, matricula: ColaboradorSchema, senha: MatriculaSchema):
    # Token CSRF se necessário
    csrf_token = get_token(request)
    
    # Usar o LoginForm para validação
    form = LoginForm({"matricula": matricula, "senha": senha})
    if form.is_valid():
        # Sucesso no login
        mensagem = form.login()
        return JsonResponse({
            "success": True,
            "message": "Login bem-sucedido!",
            "redirect_url": "/pagina_opcoes/",
            "csrfToken": csrf_token
        })
    else:
        # Erros de validação
        return JsonResponse({
            "success": False,
            "errors": form.errors,
            "csrfToken": csrf_token
        }, status=400)
