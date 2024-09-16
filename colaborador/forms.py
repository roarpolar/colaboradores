from django import forms
from .models import Matricula
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    matricula = forms.CharField(max_length=30, label="Matrícula")
    senha = forms.CharField(max_length=6, label="Senha", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        matricula = cleaned_data.get("matricula")
        senha = cleaned_data.get("senha")

        if not matricula or not senha:
            raise ValidationError("Matrícula e senha são obrigatórios.")

        try:
            # Valida a existência da matrícula
            matricula_obj = Matricula.objects.get(numero=matricula)
        except Matricula.DoesNotExist:
            raise ValidationError("Matrícula inválida.")

        colaborador = matricula_obj.colaborador

        if colaborador.senha != senha:
            raise ValidationError("Senha incorreta.")

        return cleaned_data

    def login(self):
        # Após a validação, exibe a mensagem de sucesso
        matricula = self.cleaned_data['matricula']
        colaborador = Matricula.objects.get(numero=matricula).colaborador
        return f"Login bem-sucedido! Bem-vindo, {colaborador.nome}."