from rich import print
from rich.panel import Panel
class Game:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []  

    def adicionar_jogo(self, jogo):
        self.jogos_favoritos.append(jogo)

    def mostrar_ficha(self):
        lista_formatada = "\n".join(self.jogos_favoritos)
        conteudo = f"👤 [bold]Nome:[/bold] {self.nome}\n"
        conteudo += f"🎮 [green]Nick:[/green] {self.nick}\n\n"
        conteudo += f"⭐️ [yellow]Jogos Favoritos:[/yellow]\n{lista_formatada}"
        painel = Panel(conteudo, title="FICHA DO GAMER", border_style="magenta")
        print(painel)

# Declaração de objetos
g1 = Game(nome="Davi", nick="cruzeiro_cabuloso")
g1.adicionar_jogo("FIFA 26")
g1.adicionar_jogo("NBA 2K26")
g1.adicionar_jogo("Red Dead Redemption 2")
g1.mostrar_ficha()

g2 = Game(nome="Lineker", nick="minato14")
g2.adicionar_jogo("Clash of Clans")
g2.adicionar_jogo("Call Of Duty")
g2.adicionar_jogo("God of War")
g2.mostrar_ficha()