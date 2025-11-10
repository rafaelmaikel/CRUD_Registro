from django.contrib import admin
from django.urls import include, path

# O arquivo de URLs principal do projeto faz a ligação com o aplicativo
# CRUD_Registro e define a rota de administração.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Direciona a raiz do site ("/") para as URLs do aplicativo de cadastro
    path('', include('CRUD_Registro.urls')),
]