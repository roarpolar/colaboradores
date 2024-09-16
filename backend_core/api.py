# backend_core/api.py
from ninja import NinjaAPI
from colaborador.api import colaborador_router

api = NinjaAPI()

# Adicione os routers à API
api.add_router("/colaborador/", colaborador_router)
#api.add_router("/pagina_opcoes/", matricula_router)
