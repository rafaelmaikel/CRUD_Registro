from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD_Registro.urls')),  # faz a raiz ir para o app
]
