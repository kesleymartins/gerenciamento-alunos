from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('criar-aluno', views.criar_aluno, name="criar_aluno"),
    path('alunos-cadastrados', views.alunos_cadastrados, name="alunos_cadastrados"),
    path('mostrar-aluno/<str:pk>', views.mostrar_aluno, name="mostrar_aluno"),
]