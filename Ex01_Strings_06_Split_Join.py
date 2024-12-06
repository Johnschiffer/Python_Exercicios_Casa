frase = 'Olá, bem-vindo a este treinamento'

print('-'*50)

print(frase.split()) # Encontra todos os espaços na string e separa em uma lista
print(frase.split(',')) # Encontra todas as ',' na string e separa em uma lista
print(frase.split('-')) # Encontra todas as '-' na string e separa em uma lista

print('-'*50)

nomes = 'John, Rafael, Matheus, Richard, Vitor'
print(nomes.split()) # Encontra todos os espaços na string e separa em uma lista
print(nomes.split(',')) # Encontra todas as ',' na string e separa em uma lista

print('-'*50)

hastags = 'music #guitar #gamer #coder #python'
print(hastags.split()) # Encontra todos os espaços na string e separa em uma lista
print(hastags.split('#')) # Encontra todas as '#' na string e separa em uma lista
print(hastags.split('#', 3)) # Encontra todas as '#' e para ao encontrar 3 # na string e separa em uma lista

print('-'*50)

# Como concatenar(combinar) strings
hastags = hastags.split() # Encontra todos os espaços na string e separa em uma lista

print(','.join(hastags)) # Junta as strings separando com virgula
print('.'.join(hastags)) # Junta as strings separando com ponto
print(' '.join(hastags)) # Junta as strings separando com espaço