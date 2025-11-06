from django.db import models
from django.contrib.auth.models import User

# ========================
# PERFIL (base)
# ========================
class Perfil(models.Model):
    # Definindo as opções para o campo 'tipo'
    TIPO_CHOICES = [
        ('profissional', 'Profissional'),
        ('cliente', 'Cliente'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfil_app')
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES, null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.CharField(max_length=255, blank=True, null=True)
    visivel = models.BooleanField(default=True)

    class Meta:
        managed = False  # Diz ao Django para não gerenciar esta tabela (ela já existe)
        db_table = 'perfil'

    def __str__(self):
        return self.user.username

# ========================
# CLIENTE
# ========================
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.perfil.user.username

# ========================
# PROFISSIONAL
# ========================
class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, unique=True)
    area_atuacao = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    nota_media = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    bio = models.TextField(blank=True, null=True)
    imagem_portfolio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profissional'

    def __str__(self):
        return self.perfil.user.username

# ========================
# FERRAMENTAS
# ========================
class Ferramenta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco_diaria = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    imagem = models.CharField(max_length=255, blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'ferramenta'

    def __str__(self):
        return self.nome
