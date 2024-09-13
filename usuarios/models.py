import random
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validar_cpf(cpf):
    # Adicione aqui a lógica para validar o CPF
    pass

# Modelo Colaborador
class Colaborador(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])  # CPF com validação
    data_nasc = models.DateField()  # Campo para a data de nascimento
    imagem = models.ImageField(upload_to="icones", null=True, blank=True)  # Foto é opcional
    senha = models.CharField(max_length=6, unique=True, blank=True, null=True)  # Senha de 6 dígitos não repetidos

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.senha:
            self.senha = self.gerar_senha()
        super().save(*args, **kwargs)

    def gerar_senha(self):
        """Gera uma senha de 6 números únicos"""
        while True:
            senha = ''.join(random.sample('0123456789', 6))
            if not Colaborador.objects.filter(senha=senha).exists():
                return senha

# Modelo Matricula
class Matricula(models.Model):
    numero = models.CharField(max_length=30, unique=True)  # Número da matrícula, único
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="matriculas")
    funcao_atual = models.CharField(max_length=30)  # Função atual do colaborador
    data_inicio = models.DateField()  # Data de início dessa matrícula
    data_fim = models.DateField(null=True, blank=True)  # Data de término (caso a matrícula seja encerrada)
    historico_funcoes = models.TextField(null=True, blank=True)  # Histórico de funções do colaborador

    def __str__(self):
        return f"Matrícula: {self.numero} - {self.colaborador.nome}"

    def adicionar_mudanca_funcao(self, nova_funcao):
        """Adiciona a mudança de função no histórico e atualiza a função atual"""
        data_mudanca = timezone.now().date()
        mudanca = f"Mudança para: {nova_funcao} em {data_mudanca}"
        
        if self.historico_funcoes:
            self.historico_funcoes += f"\n{mudanca}"
        else:
            self.historico_funcoes = mudanca
        
        self.funcao_atual = nova_funcao  # Atualiza a função atual
        self.save()

