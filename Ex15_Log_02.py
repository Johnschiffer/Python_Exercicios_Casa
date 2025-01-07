import logging

#Salvar log em um arquivo
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s -%(asctime)s')


# Try e Except serve para não mostrar erro ao usuario
try:
    email = input('Digite seu email: ')
    senha = int(input('Digite sua senha: '))

    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} entrou em sua conta')
    
    else:
        logging.info(f'{email} digitou a senha errada')

except ValueError as erro:
    print('Favor Digitar apenas numero!')
    logging.warning(erro)
