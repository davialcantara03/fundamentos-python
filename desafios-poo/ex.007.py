import time
from rich import print
from rich.panel import Panel

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1  # Todo livro começa na página 1

    def avancar_pagina(self):
        if self.pagina_atual < self.total_paginas:
            conteudo = f"📖 Lendo a página [bold yellow]{self.pagina_atual}[/bold yellow] de {self.total_paginas}..."
            print(Panel(conteudo, title=self.titulo, border_style="blue"))
            time.sleep(0.3) 
            self.pagina_atual += 1
            print(f"➡️ [green]Você virou a página! Agora está na página {self.pagina_atual}.[/green]\n")
        
        elif self.pagina_atual == self.total_paginas:
            print(f"🎉 [bold gold1]Parabéns! Você chegou à página {self.pagina_atual} e FINALIZOU a leitura de '{self.titulo}'![/bold gold1] 🏆\n")
            self.pagina_atual += 1 # Vai para a "página final" para travar o livro
            
        else:
            print(f"❌ [red]Ops! Você já terminou de ler '{self.titulo}'. Não há mais páginas para avançar.[/red]\n")

meu_livro = Livro(titulo="O Segredo dos Dados", total_paginas=50)

for i in range(50):
    meu_livro.avancar_pagina()