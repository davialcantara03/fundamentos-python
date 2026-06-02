from rich import print
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True 

    def escrever(self, texto):
        if self.tampada:
            print(f"Erro: A [{self.cor}]caneta[/{self.cor}] está tampada! Não dá para escrever.")
        else:
            print(f"[{self.cor}]{texto}[/{self.cor}]")

    def tampar(self):
        self.tampada = True
        print(f"A [bold]caneta[/bold] está tampada.")

    def destampar(self):
        self.tampada = False
        print(f"A [bold]caneta[/bold] foi destampada.")

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd, end='')
# Declaração de Objetos
caneta_azul = Caneta(cor="blue")
caneta_verde = Caneta(cor="green")
caneta_vermelha = Caneta(cor="red")
caneta_azul.escrever("HOJE TEM GOL DO KAIO JORGE")
caneta_verde.escrever("PELO HEXA!")
caneta_vermelha.escrever("FUNCIONOU!")
print("-" * 30)
caneta_azul.destampar()
caneta_azul.quebrar_linha(1)
caneta_verde.destampar()
caneta_vermelha.destampar()
caneta_azul.escrever("HOJE TEM GOL DO KAIO JORGE")
caneta_verde.escrever("PELO HEXA!")
caneta_vermelha.escrever("FUNCIONOU!")
