# CRUD_Registro/models.py
from django.db import models

class Cargo(models.Model):
    nome = models.CharField("Nome do cargo", max_length=50)

    class Meta:
        verbose_name = "cargo"
        verbose_name_plural = "cargos"

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField("Nome do departamento", max_length=100)
    sigla = models.CharField("Sigla", max_length=10, unique=True)

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"

    def __str__(self):
        return self.nome

# CRUD_Registro/models.py
class Empregado(models.Model):
    nome_completo = models.CharField("Nome completo", max_length=100)
    codigo = models.CharField("Código", max_length=3, unique=True)
    telefone = models.CharField("Telefone", max_length=15)
    cargo = models.ForeignKey(
        Cargo,
        verbose_name="Cargo",
        on_delete=models.PROTECT,
        related_name="empregados",
        null=True,      # permitir valor NULL no banco
        blank=True      # permitir deixar em branco nos formulários
    )
    departamento = models.ForeignKey(
        Departamento,
        verbose_name="Departamento",
        on_delete=models.PROTECT,
        related_name="empregados",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "empregado"
        verbose_name_plural = "empregados"

    def __str__(self):
        return f"{self.nome_completo} ({self.codigo})"