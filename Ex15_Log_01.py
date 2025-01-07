import logging

# debug - Informação para desenvolvedores

# info - Informação de algo que está acontecendo no programa mas não é um Error

# warning - Alerta sobre algo fora do esperado mas não é um erro 

# error - Um erro na aplicação

# critical - Erro com graves consequencias na aplicação


#Salvar log em um arquivo
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s')

logging.debug('Logging no nível debug')
logging.info('Logging no nível info')
logging.warning('Logging no nível warning')
logging.error('Logging no nível error')
logging.critical('Logging no nível critical')