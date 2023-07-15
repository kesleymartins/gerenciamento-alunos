from django.shortcuts import render, redirect
from django.http import request
from .forms import AlunoForm

def index(request):
    context = {}
    return render(request, 'index.html', context)

def criar_aluno(request):
    form = AlunoForm()

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('alunos_cadastrados')

    context = { 'form': form }
    return render(request, 'criar-aluno.html', context)

def alunos_cadastrados(request):
    context = {}
    return render(request, 'alunos-cadastrados.html', context)

def mostrar_aluno(request, pk):
    context = {}
    return render(request, 'mostrar-aluno.html', context)
