from django.db import models

class Position(models.Model):
    title = models.CharField("Título", max_length=50)

    class Meta:
        verbose_name = "cargo"
        verbose_name_plural = "cargos"

    def __str__(self):
        return self.title

class Empregado(models.Model):
    nome_completo = models.CharField("Nome completo", max_length=100)
    codigo = models.CharField("Código", max_length=3)
    numero = models.CharField("Telefone", max_length=15)
    # Se o cargo for opcional, adicione blank=True e null=True
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,       # ou SET_NULL, conforme a sua lógica
        related_name="empregados",
        verbose_name="Cargo",
    )

    class Meta:
        verbose_name = "empregado"
        verbose_name_plural = "empregados"

    def __str__(self):
        return f"{self.nome_completo} ({self.codigo})"