# Trabalhando com Multiplas listas
from itertools import zip_longest


produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]

for a, b in zip(produtos, precos):
    print(f'Salvando produto {a} valor R$ {b}')


# Quando uma lista é menor que a outra, usaremos o zip_longest
titulos = ['Título 1', 'Título 2', 'Título 3', 'Título 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} descrição: {descricao}')