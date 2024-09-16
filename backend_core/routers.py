from ninja import Router
import requests
# Defina o router para usuários
colaborador_router = Router()

@colaborador_router.get("/login")
def list_colaboradores(request):
    return {"message": "List of users"}

# Defina o router para página de opções
opcoes_pagina_router = Router()

@opcoes_pagina_router.get("/pagina_opcoes/")
def pagina_opcoes(request):
    return {"message": "Página de opções"}  # Ajuste conforme necessário
