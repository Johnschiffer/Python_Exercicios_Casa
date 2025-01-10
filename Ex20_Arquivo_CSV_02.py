from csv import DictReader, DictWriter

# Cria um CSV chamado pessoas usando dict writer, esse arquivo deve conter o seguinte formato:
# nome,idade,altura
# Mark,25,170
# Carol,19,160
# Robert,65,175
with open('Ex20_Arquivo_CSV_02/pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
    cabecalho = ['Nome', 'Idade', 'Altura']
    csv_whriter = DictWriter(arquivo, fieldnames=cabecalho)
    csv_whriter.writeheader()
    csv_whriter.writerow({
        'Nome': 'Mark',
        'Idade': 25,
        'Altura': 170
    }),
    csv_whriter.writerow({
        'Nome': 'Carol',
        'Idade': 19,
        'Altura': 160
    }),
    csv_whriter.writerow({
        'Nome': 'Robert',
        'Idade': 65,
        'Altura': 175
    })


# Agora modifique adicionando cm ao finalde altura
with open('Ex20_Arquivo_CSV_02/pessoas.csv', 'r', newline='', encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    pessoas = list(dados_originais)
    
    with open('Ex20_Arquivo_CSV_02/pessoas_alterado.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
        cabecalho = ['Nome', 'Idade', 'Altura']
        csv_whriter = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_whriter.writeheader()

        for pessoa in pessoas:
            csv_whriter.writerow({
                'Nome': pessoa['Nome'],
                'Idade': pessoa['Idade'],
                'Altura': pessoa['Altura'] + ' cm',
            })