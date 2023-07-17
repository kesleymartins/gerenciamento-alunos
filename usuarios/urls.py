from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="usuario.cadastro"),
    path('login/', views.login, name="usuario.login"),
    path('sair/', views.logout, name="usuario.logout"),
]