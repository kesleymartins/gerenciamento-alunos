from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno

def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url="/auth/login")
def criar_aluno(request):
    form = AlunoForm()

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('alunos_cadastrados')

    context = { 'form': form }
    return render(request, 'criar-aluno.html', context)

@login_required(login_url="/auth/login")
def alunos_cadastrados(request):
    alunos = Aluno.objects.all()
    context = { 'alunos': alunos }
    return render(request, 'alunos-cadastrados.html', context)

def mostrar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    context = { 'aluno': aluno }
    return render(request, 'mostrar-aluno.html', context)
