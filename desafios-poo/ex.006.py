from rich import print
from rich.panel import Panel
# Declaração de Classes
class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, título, quant):
        # Atributos de Instância
        self.título = título
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.título} com {self.participantes} pessoas participando."

    def calcular_qtd_carne(self):
        return self.participantes * Churrasco.consumo_padrao 

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando {self.título} com {self.participantes} convidados"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R$ {Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de carne"
        conteudo += f"\nO custo total será de R${self.calcular_custo_total():,.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calcular_custo_individual():,.2f}"
        painel = Panel(conteudo, title=self.título)
        print(painel)

c1 = Churrasco(título="Churras dos Amigos", quant=15)
c1.analisar()