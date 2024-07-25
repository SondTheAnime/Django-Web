from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    