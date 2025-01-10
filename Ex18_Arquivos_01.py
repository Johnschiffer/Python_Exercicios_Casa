import os

print(os.name) # Listar OS
print(os.listdir) # Listar arquivos no diretorio atual
print(os.getcwd) # Retorna patch do diretorio atual
print(os.sep) # Retorna o separador nativo do OS atual

# Retorna patch do arquivo
print(os.path.join(os.getcwd() + os.sep + 'README.md'))

# Retorna patch de arquivo em sub-pasta
print(os.path.join(os.getcwd() + os.sep + 'documentos' + os.sep + 'musica.mp3'))

caminho = os.path.join(os.getcwd() + os.sep + 'README.md')
print(os.path.dirname(caminho)) # Obter o diretorio de um path
print(os.path.basename(caminho)) # Obter arquivo de um path
print(os.path.exists(os.getcwd() + os.sep + 'documentos'))