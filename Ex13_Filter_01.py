# Filter extrai apenas o item com uma condição especifica

nomes = ['Mateus', 'Rafael', 'Richard', 'John']

def pessoas_aprovadas(pessoa):
    if pessoa == 'John':
        return True
    else:
        return False
    
print(list(filter(pessoas_aprovadas, nomes))) # Extrai apenas o item especifico
print(list(map(pessoas_aprovadas, nomes))) # Extrai todos itens da lista

print('-'*50)

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897],
]

def antiguidade(pintura):
               # Busca apenas no indice 2 da lista
    if pintura[2] < 1890:
        return True
    else:
        return False
print(list(filter(antiguidade, pinturas)))
