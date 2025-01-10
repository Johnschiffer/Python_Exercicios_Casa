import os


print('-'*50)
# Exibe todos arquivos naquela pasta
print(os.listdir(os.getcwd() + os.sep + 'Ex18_Arquivos_02' + os.sep + 'desafio arquivos'))

print('-'*50)
# Exibe o caminho(PATH) dos 3 arqvuiso da pasta atual
print(os.path.join(os.getcwd() + os.sep + 'Ex18_Arquivos_02' + os.sep + 'desafio arquivos'))

print('-'*50)
# Exibe o caminho(PATH) dos 3 arqvuiso da sub-pasta
print(os.path.join(os.getcwd() + os.sep + 'Ex18_Arquivos_02' + os.sep + 'desafio arquivos' + os.sep + 'desafio texto'))

print('-'*50)
