from ninja import Router 
from ninja import ModelSchema, Schema 
from .models import Api
from typing import Optional, List
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.http import JsonResponse  
from .models import Colaborador, Matricula
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt 
from ninja import Router
from typing import List
from ninja import Schema

router = Router()


class ColaboradorSchema(Schema):
    id: int
    nome: str
    data_nasc: str

class MatriculaSchema(Schema):
    id: int
    numero: int
    matricula: int
   


#@csrf_exempt  # Desativa CSRF para esta rota
@router.post("/login/")
def login_view(request, colaborador: str, senha: str):
    # Token CSRF se necessário
    csrf_token = get_token(request)
    
    # Usar o LoginForm para validação
    form = LoginForm({"colaborador": colaborador, "senha": senha})
    if form.is_valid():
        # Sucesso no login
        mensagem = form.login()
        return JsonResponse({
            "success": True,
            "message": mensagem,
            "redirect_url": "/pagina_inicial/",
            "csrfToken": csrf_token
        })
    else:
        # Erros de validação
        return JsonResponse({
            "success": False,
            "errors": form.errors,
            "csrfToken": csrf_token
        }, status=400)
