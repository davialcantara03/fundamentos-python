from transporte import Caminhao, Moto, Drone
from rich import print, inspect
from rich.table import Table

def main():
    dist = 80
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância", justify="center")
    tabela.add_column("Tipo", justify="left")
    tabela.add_column("Frete", justify="right")

    for item in viagem: 
        nome_transporte = item.__class__.__name__
        valor_frete = item.calcular_frete()
        tabela.add_row(f"{dist} Km", nome_transporte, f"{valor_frete}")
    print(tabela)

if __name__ == "__main__":
    main()