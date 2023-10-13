from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Tipos(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nome
    
class Transacao(models.Model):
    banco = models.CharField(max_length=30, null=True, blank=True)
    tipo = models.ForeignKey(Tipos, null=True, blank=True, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True,  blank=True)
    descricao = models.CharField(max_length=200, null=True,  blank=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, null=True,  blank=True)
    categoria = models.ForeignKey(Categoria, null=True,  blank=True, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.descricao