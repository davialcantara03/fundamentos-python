from rich import print
from rich.panel import Panel
# Declaração de Classes
class Produto:
    def __init__(self, nome, preço): # Método construtor
        self.nome = nome
        self.preço = preço

    def __str__(self):
        return f'{self.nome} custa {self.preço:,.2f}'

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}\n"
        conteudo += f"{'-' * 30}\n"
        precof = f"R${self.preço:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta_visual = Panel(conteudo, title="Produto", width=34)
        print(etiqueta_visual)

# Declaração de objetos
p1 = Produto(nome="Iphone 17 Pro Max", preço=25_000.85)
print(p1)
p1.etiqueta()
p2 = Produto(nome="Notebook Gamer", preço=8_000)
p2.etiqueta()