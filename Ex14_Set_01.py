# SET
frutas = {'Maçã', 'Uva', 'Banana', 'Morango', 'Maçã'}
# Convertendo para set
# Remove itens duplicados
set_frutas = set(frutas)
print(set_frutas)

print('-'*50)

# Adicionando novos valores
numeros = [2, 2, 5, 8]
set_numeros = set(numeros)
set_numeros.add(10)
print(set_numeros)

print('-'*50)

# Conjuntos de set
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]

a = set(numeros1)
b = set(numeros2)

# Valores unicos entre os 2 set
print(a.symmetric_difference(b))

# Valores em comum entre sets
print(a.intersection(b))

# Une valores UNICOS entre sets
print(a.union(b))
