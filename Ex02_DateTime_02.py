from datetime import datetime

aniversario = datetime.strptime(input("Data do seu aniversário: "), '%d/%m/%Y')

# Quanto tempo até a data do seu aniversario
data_atual = datetime.now()
prazo = aniversario - data_atual
print(f'Faltam {prazo.days} dias para seu aniversário.')