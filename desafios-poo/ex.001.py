# Declaração de Classes
class Gafanhoto: 
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ''
        self.idade = 0

    # Método de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos.'

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 20
g1.aniversario() # Chamada do método de instância
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario() # Chamada do método de instância
print(g2.mensagem())