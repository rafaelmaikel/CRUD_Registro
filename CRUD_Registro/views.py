from django.shortcuts import render, redirect, get_object_or_404
from .models import Cargo, Departamento, Empregado
from .forms import CargoForm, DepartamentoForm, EmpregadoForm

# ------ CARGOS ------
def cargo_list(request):
    cargos = Cargo.objects.all()
    return render(request, "CRUD_Registro/cargo_list.html", {"cargos": cargos})

def cargo_create(request):
    if request.method == "POST":
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cargo_list")
    else:
        form = CargoForm()
    return render(request, "CRUD_Registro/cargo_form.html", {"form": form})

def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == "POST":
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect("cargo_list")
    else:
        form = CargoForm(instance=cargo)
    return render(request, "CRUD_Registro/cargo_form.html", {"form": form})

def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == "POST":
        cargo.delete()
        return redirect("cargo_list")
    return render(request, "CRUD_Registro/cargo_confirm_delete.html", {"cargo": cargo})

# ------ DEPARTAMENTOS ------
def departamento_list(request):
    departamentos = Departamento.objects.all()
    return render(request, "CRUD_Registro/departamento_list.html", {"departamentos": departamentos})

def departamento_create(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departamento_list")
    else:
        form = DepartamentoForm()
    return render(request, "CRUD_Registro/departamento_form.html", {"form": form})

def departamento_update(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect("departamento_list")
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, "CRUD_Registro/departamento_form.html", {"form": form})

def departamento_delete(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        departamento.delete()
        return redirect("departamento_list")
    return render(request, "CRUD_Registro/departamento_confirm_delete.html", {"departamento": departamento})

# ------ EMPREGADOS ------
def empregado_list(request):
    empregados = Empregado.objects.select_related("cargo", "departamento").all()
    return render(request, "CRUD_Registro/empregado_list.html", {"empregados": empregados})

def empregado_create(request):
    if request.method == "POST":
        form = EmpregadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empregado_list")
    else:
        form = EmpregadoForm()
    return render(request, "CRUD_Registro/empregado_form.html", {"form": form})

def empregado_update(request, pk):
    empregado = get_object_or_404(Empregado, pk=pk)
    if request.method == "POST":
        form = EmpregadoForm(request.POST, instance=empregado)
        if form.is_valid():
            form.save()
            return redirect("empregado_list")
    else:
        form = EmpregadoForm(instance=empregado)
    return render(request, "CRUD_Registro/empregado_form.html", {"form": form})

def empregado_delete(request, pk):
    empregado = get_object_or_404(Empregado, pk=pk)
    if request.method == "POST":
        empregado.delete()
        return redirect("empregado_list")
    return render(request, "CRUD_Registro/empregado_confirm_delete.html", {"empregado": empregado})