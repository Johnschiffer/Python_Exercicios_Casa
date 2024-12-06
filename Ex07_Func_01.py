# return só é utilizado quando precisamos usar o resultado da função
# mais pra frente no programa

def calcular_valores(valor, quantidade=1):
    print(f'Valor total: {valor * quantidade}')

preco = int(input("Digite o valor: "))
quant = int(input("Digite a quantidade: "))

calcular_valores(preco, quant)
