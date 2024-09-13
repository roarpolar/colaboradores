from ninja import Router, Schema
from typing import List
import datetime

colaborador_router = Router()

class ColaboradorSchema(Schema):
    nome: str
    cpf: str
    data_nasc: datetime.date
    imagem: str = None

class MatriculaSchema(Schema):
    numero: str
    colaborador: int
    funcao_atual: str
   

