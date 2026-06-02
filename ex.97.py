def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(texto.center(tam))
    print('~' * tam)


# PROGRAMA PRINCIPAL:
escreva('Davi')
escreva('Cruzeiro')
escreva('CEC')