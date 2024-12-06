# continue e pass

# Ao encontrar Rap, pular para o proximo
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

for i in estilos:
    if i == 'Rap':
        continue

    print(i)

print('-'*50)

# Ao encontrar Rock parar a iteração
for i in estilos:
    if i == 'Rock':
        break
    print(i)