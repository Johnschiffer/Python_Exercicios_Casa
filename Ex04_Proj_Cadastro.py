# Obtenha o nome do usuario e idade, registre a data do cadastro e para cada cadastro
# o usuario recebe um cartão aleatorio


import random
from datetime import datetime

cartoes = ['R$ 50.00', 'R$ 250,00', 'R$ 120,00']

nome = (input("Digite seu nome: "))
idade = (input("Digite sua idade: "))

aniversario = datetime.strptime(input("Data do seu aniversário: "), '%d/%m/%Y')
data_cadastro = datetime.now()

print(f'Olá, {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.strftime("%d/%m/%Y")}\n'
      f'Parabéns, houve um sorteio e você ganhou um cartão de credito de {random.choice(cartoes)}')

