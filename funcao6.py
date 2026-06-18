def desconto(preco=0.0, taxa=0.0):
    """a função desconto calcula o valor de desconto 
    de um determinado preço """
    return preco * taxa / 100


rs = desconto(500,4.2)
print(f"o valor do desconto é {rs}")







desconto()