from rich import print
from rich import inspect
# Declaração de Classes
class Funcionarios:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo): # Método construtor
        self.nome = nome 
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f':handshake: Olá, sou [bold blue]{self.nome}[/bold blue] e sou {self.cargo} do setor de {self.setor} na empresa {Funcionarios.empresa}'

# Declaração de objetos
c1 = Funcionarios(nome="Maria", setor="Administração", cargo="Diretora")
c2 = Funcionarios(nome="Pedro", setor="TI", cargo="Programador")
print(c1.apresentar())
print(c2.apresentar())
#inspect(c1)
#inspect(c2)