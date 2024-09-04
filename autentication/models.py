from django.db import models

class Colaborador(models.Model):
    colaborador = models.CharField(max_length=30)
    matricola = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to="icones", null=True, blank=True)
def __str__(self):
    return self.colaborador


