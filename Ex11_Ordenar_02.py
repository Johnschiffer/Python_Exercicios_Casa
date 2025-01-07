from operator import itemgetter

produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]

# Ordenar tuplas será por indice
produtos.sort(key=itemgetter(1)) # produtos.sort(key=itemgetter(1), reverse=True) Para ordenar reverso 
print(produtos)