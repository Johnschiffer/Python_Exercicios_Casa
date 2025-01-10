from csv import DictReader, DictWriter

# Ler um arquivo CSV
# with open('DESTINO') as arquivo:
#     dados = DictReader(arquivo)
#     for dado in dados:
#         print(dado)




# Criar um arquivo CSV
with open('Ex20_Arquivo_CSV_01/computadores.csv', 'w', newline='', encoding='utf-8') as arquivo:
    cabecalho = [ 'Marca', 'Preço', 'Ano de Lançamento']
    csv_whriter = DictWriter(arquivo, fieldnames=cabecalho)
    csv_whriter.writeheader()
    csv_whriter.writerow({
        'Marca': 'Asus',
        'Preço': '2500',
        'Ano de Lançamento': 2025
    }),
    csv_whriter.writerow({
        'Marca': 'Dell',
        'Preço': '1500',
        'Ano de Lançamento': 2025
    }),
    csv_whriter.writerow({
        'Marca': 'ACER',
        'Preço': '3500',
        'Ano de Lançamento': 2025
    })