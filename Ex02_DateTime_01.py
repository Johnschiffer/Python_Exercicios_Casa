from datetime import datetime

print(datetime.now()) # Hora atual
print(datetime.now().day) # Dia atual
print(datetime.now().month) # Mês atual
print(datetime.now().year) # Ano atual

# Criar uma data
lancamento_app = datetime(2024, 12, 10)
print(lancamento_app)

# Quero recerber a data de lançamento do app
data_lancamento = datetime.strptime(input("Data lançamento?: "), '%d/%m/%Y')

# Quanto tempo até a data de lançamento do app
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(f'Faltam {prazo.days} dias.')