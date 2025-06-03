from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Produto(models.Model):  # Certifique-se de que este já existe
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(auto_now_add=True)

    def valor_total(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return f"{self.cliente.nome} - {self.produto.nome}"