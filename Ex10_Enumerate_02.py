# Enumerate
# Adicionar um contador a um objeto iterável
# Saber a posição de um elemento em uma sequência 

frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']
                                       # Inicia o indice enumerate em 0
for indice, fruta in enumerate(frutas, 0):
    print(indice, fruta)
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO!')