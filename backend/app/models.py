from django.db import models
from django.contrib.auth.models import User

# ========================
# PERFIL (base)
# ========================
class Perfil(models.Model):
    TIPO_CHOICES = [
        ('profissional', 'Profissional'),
        ('cliente', 'Cliente'),
    ]
    id = models.AutoField(primary_key=True)
    # Coluna do seu SQL: user_id (ForeignKey para auth_user)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfil_app', db_column='user_id')
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES, null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    # Coluna do seu SQL: imagem VARCHAR(255)
    imagem = models.CharField(max_length=255, blank=True, null=True)
    visivel = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'perfil'

    def __str__(self):
        return self.user.username

# ========================
# CLIENTE
# ========================
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    # Coluna do seu SQL: perfil_id (OneToOne para perfil)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, unique=True, db_column='perfil_id')
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
    # Coluna do seu SQL: perfil_id (OneToOne para perfil)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, unique=True, db_column='perfil_id')
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
    # Coluna do seu SQL: imagem VARCHAR(255)
    imagem = models.CharField(max_length=255, blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'ferramenta'

    def __str__(self):
        return self.nome

# ========================
# SERVIÇO (Agora "Não Gerenciado")
# ========================
class Servico(models.Model):
    # Coluna do seu SQL: profissional_id (ForeignKey para profissional)
    # CORREÇÃO: O prestador é um 'Profissional', não um 'Perfil'
    prestador = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='servicos', db_column='profissional_id')
    
    # catalogo_id é ignorado por enquanto
    
    titulo = models.CharField(max_length=100) # Seu SQL usa 100
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) # Seu SQL usa 8,2
    
    # Coluna do seu SQL: imagem VARCHAR(255)
    # MUDANÇA: 'foto' agora é 'CharField' para bater com seu SQL.
    # Isso significa que você NÃO precisa do Pillow ou do MEDIA_ROOT.
    # Seu formulário 'novo_servico.html' deve salvar um link (URL) aqui, não um arquivo.
    foto = models.CharField(max_length=255, blank=True, null=True, db_column='imagem')
    
    aprovado = models.BooleanField(default=False)
    
    # data_criacao foi removido (não existe no seu SQL 'servico')

    class Meta:
        managed = False
        db_table = 'servico'

    def __str__(self):
        return self.titulo

# ========================
# AGENDAMENTO (Agora "Não Gerenciado")
# ========================
class Agendamento(models.Model):
    # Coluna do seu SQL: servico_id (ForeignKey para servico)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos', db_column='servico_id')
    
    # Coluna do seu SQL: cliente_id (ForeignKey para cliente)
    # CORREÇÃO: O cliente é um 'Cliente', não um 'Perfil'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos', db_column='cliente_id')
    
    # Coluna do seu SQL: data DATE
    data_agendamento = models.DateField(db_column='data')
    
    # Coluna do seu SQL: horario TIME
    horario = models.TimeField()
    
    status = models.CharField(max_length=20, default='Agendado')
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
    # data_criacao foi removido (não existe no seu SQL 'agendamento')

    class Meta:
        managed = False
        db_table = 'agendamento'

    def __str__(self):
        return f'Agendamento de {self.servico.titulo} para {self.cliente.perfil.user.username}'