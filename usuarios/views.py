from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'cadastro.html', {})

        user = User.objects.create_user(username, "", password)
        user.save()

        django_login(request, user)

        return redirect('alunos_cadastrados')

    return render(request, 'cadastro.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('alunos_cadastrados')

    return render(request, 'login.html', {})

def logout(request):
    django_logout(request)
    return redirect('home_page')
