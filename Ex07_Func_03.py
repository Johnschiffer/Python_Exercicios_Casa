def somar(*valores, b):
    print(valores)

    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 5, b=5) # Ultimo parametro tem que ser nomeado

# *args (Passa diversos paramentos para a função que armazena em formato de tupla)