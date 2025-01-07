# Ordene a lista pelo preço em ordem crescente

from operator import itemgetter

produtos = [
    {'nome': 'Celular',
     'preco': 1500},
     {'nome': 'Monitor',
     'preco': 500},
     {'nome': 'Microfone',
     'preco': 300},
]

produtos.sort(key=itemgetter('preco'))
print(produtos)