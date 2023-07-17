from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('alunos.urls')),
    path('auth/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
