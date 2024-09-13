# backend_core/routers.py
from .api import api
from ninja import Router

# Defina o router
usuarios_router = Router()

@usuarios_router.get("/list")
def list_usuarios(request):
    return {"message": "List of users"}

# Adicione o router à API
api.add_router('/usuarios/', usuarios_router)
