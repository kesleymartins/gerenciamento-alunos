from django.shortcuts import render
from django.http import request
from .forms import AlunoForm

def index(request):
    context = {}
    return render(request, 'index.html', context)

def criar_aluno(request):
    form = AlunoForm()
    context = { 'form': form }
    return render(request, 'criar-aluno.html', context)

def alunos_cadastrados(request):
    context = {}
    return render(request, 'alunos-cadastrados.html', context)

def mostrar_aluno(request, pk):
    context = {}
    return render(request, 'mostrar-aluno.html', context)
