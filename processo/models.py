from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    Nome = models.CharField(max_length=150, null=True, blank=True)
    Data_Nascimento = models.DateField(null=True, blank=True)
    CPF = models.CharField(max_length=11, null=True, blank=True)
class Funcionario(Pessoa):
    Carteira_de_Trabalho = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Nome

class Departamento(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Usuario')
    interessados = models.ManyToManyField(Pessoa, related_name='Interessados')
    investigados = models.ManyToManyField(Pessoa, related_name='Investigados')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return  self.numero

class Documento(models.Model):
    Usuario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    Processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    Numero = models.CharField(max_length=15)
    Titulo = models.CharField(max_length=20)
    Data = models.DateField()
    Texto = models.TextField()


    def __str__(self):
        return self.Numero

class Portaria(Documento):
    instauracao = models.TextField()

    def __str__(self):
        return self.numero

class Pedido(Documento):
    prazoAnterior = models.DateField()
    prazoNovo = models.DateField()
    justificativa = models.TextField()

    def __str__(self):
        return self.numero

class Envio(Documento):
    dataEnvio = models.DateField()
    departamento = models.OneToOneField(Departamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.numero

class Tranmitacoes(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    origem = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='DepartamentoOrigem')
    dataSaida = models.DateField()
    destino = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='DepartamentoDestino')
    dataEntrada = models.DateField()

    def __str__(self):
        return self.processo.numero
