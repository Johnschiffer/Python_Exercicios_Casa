# Transforme a frase1 em uma lista de palavras
# e guarde o resultado em uma variavel chamada palavras1

frase1 = 'Desafio manipulação de strings'
palavras1 = (frase1.split())
print(palavras1)

# Transforme a frase2 em uma lista de palavras
# e guarde o resultado em uma variavel chamada palavras2

frase2 = 'John,Rafael,Matheus,Richard'
palavras2 = (frase2.split(','))
print(palavras2)

print('-'*50)

# Transforme palavras1 em 'Desafio,manipulação,de,strings'

print((','.join(palavras1)))

# Transforme palavras2 em 'John & Rafael & Matheus & Richard'
print((' & '.join(palavras2)))