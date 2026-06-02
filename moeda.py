def moeda(preco = 0, moeda = 'R$' ):
    v_formatado = f'{moeda}{preco:>.2f}'
    v_final = v_formatado.replace('.', ',')
    return v_final

def aumentar(preco=0, taxa=0,formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(n=0, formato=False):
    res = n * 2            
    return res if formato is False else moeda(res)

def metade(n=0, formato=False): 
    res = n / 2
    return res if formato is False else moeda(res)
