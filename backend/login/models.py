from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=15, choices=[('cliente', 'Cliente'), ('profissional', 'Profissional')])
    descricao = models.TextField(blank=True, null=True)
    imagem = models.CharField(max_length=255, blank=True, null=True)
    visivel = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Cliente(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cliente: {self.perfil.user.username}"


class Profissional(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    area_atuacao = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    nota_media = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    bio = models.TextField(blank=True, null=True)
    imagem_portfolio = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Profissional: {self.perfil.user.username}"
