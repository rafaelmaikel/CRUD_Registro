# CRUD_Registro/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # CRUD de cargos
    path('cargos/', views.cargo_list, name='cargo_list'),
    path('cargos/novo/', views.cargo_create, name='cargo_create'),
    path('cargos/<int:pk>/editar/', views.cargo_update, name='cargo_update'),
    path('cargos/<int:pk>/excluir/', views.cargo_delete, name='cargo_delete'),

    # CRUD de departamentos
    path('departamentos/', views.departamento_list, name='departamento_list'),
    path('departamentos/novo/', views.departamento_create, name='departamento_create'),
    path('departamentos/<int:pk>/editar/', views.departamento_update, name='departamento_update'),
    path('departamentos/<int:pk>/excluir/', views.departamento_delete, name='departamento_delete'),

    # CRUD de empregados
    path('empregados/', views.empregado_list, name='empregado_list'),
    path('empregados/novo/', views.empregado_create, name='empregado_create'),
    path('empregados/<int:pk>/editar/', views.empregado_update, name='empregado_update'),
    path('empregados/<int:pk>/excluir/', views.empregado_delete, name='empregado_delete'),
]
