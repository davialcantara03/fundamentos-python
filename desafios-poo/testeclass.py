# Declaração de Classes
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Método de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos.'

# Declaração de objetos
g1 = Gafanhoto("Maria", 20)
g1.aniversario() # Chamada do método de instância
print(g1)

print(g1.__dict__)
print(g1.__class__)