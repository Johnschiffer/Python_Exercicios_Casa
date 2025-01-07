from operator import itemgetter

pessoas = [
    {'nome': 'John',
     'idade': 32,
     'nivel_acesso': 2},
     {'nome': 'Carol',
     'idade': 18,
     'nivel_acesso': 3},
     {'nome': 'Thomas',
     'idade': 45,
     'nivel_acesso': 3},
     {'nome': 'Amanda',
     'idade': 23,
     'nivel_acesso': 5},
     {'nome': 'Rafael',
     'idade': 25,
     'nivel_acesso': 1},
]

# Ordenar dicionario será por chave
pessoas.sort(key=itemgetter('nome')) 
print(pessoas)