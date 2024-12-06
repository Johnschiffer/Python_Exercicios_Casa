# Importa biblioteca de valores random
import random

print(random.random()) # Gera um valor de 0.0 a 1.0

# Gera um valor decimal Min e Max
print(random.uniform(4, 10))

# Gera um valor INTEIRO Min e Max
print(random.randint(4, 10))

# Escolhe um item aleatorio de uma lista
cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores))

# Escolhe DOIS itens aleatorio de uma lista
cores = ['verde', 'vermelho', 'azul']
print(random.choices(cores, k=2))

# Embaralhar uma lista

cartas = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas)
print(cartas)

