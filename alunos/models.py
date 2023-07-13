from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)

    data_nascimento = models.DateField()
    data_ingresso = models.DateField()