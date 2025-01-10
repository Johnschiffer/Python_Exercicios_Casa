import os

# Cria pasta não existente
if os.path.exists('Ex18_Arquivos_03'):
    print('Diretório já existe!')

else:
    os.mkdir('Ex18_Arquivos_03')
    
    # Cria pasta e subpastas
    os.makedirs('Ex18_Arquivos_03' + os.sep + 'Pasta1' + os.sep + 'Pasta2')


