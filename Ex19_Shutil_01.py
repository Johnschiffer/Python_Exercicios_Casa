import shutil
import os

#Copie o arquivo nomes.txt para a pasta 'Arquivos 2010'
shutil.copy(src=os.getcwd() + os.sep + 'Ex19_Shutil_01/nomes.txt', dst=os.getcwd() + os.sep + 'Ex19_Shutil_01/arquivos 2010')

#Move o arquivo inscrições.pdf para a pasta 'Documentação'
shutil.move(src=os.getcwd() + os.sep + 'Ex19_Shutil_01/inscrições.pdf', dst=os.getcwd() + os.sep + 'documentação')

#Faça uma cópia da pasta 'arquivos 2010' e tudo que estiver contido nela para uma nova pasta chamada 'Backup arquivos 2010'
shutil.copytree(src=os.getcwd() + os.sep + 'arquivos 2010', dst=os.getcwd() + os.sep + ' backup arquivos 2010')

#Compacte todo o conteúdo da pasta 'Documentação' no formato zip
shutil.make_archive('Ex19_Shutil_01/documentação', 'zip', os.getcwd() + os.sep + 'Ex19_Shutil_01/documentação')

#Mova o arquivo compactado para dentro da pasta 'backup'
shutil.move(src=os.getcwd() + os.sep + 'Ex19_Shutil_01/documentação.zip', dst=os.getcwd() + os.sep + 'Ex19_Shutil_01/backup')

#Exclua o diretório 'Arquivos 2010 e 'documentação' e seus conteúdos
shutil.rmtree(os.getcwd() + os.sep + 'Ex19_Shutil_01/arquivos 2010')
shutil.rmtree(os.getcwd() + os.sep + 'Ex19_Shutil_01/documentação')

#compacte o diretorio inteniro para um arquivo chamado ' backup arquivos Python.zip
shutil.make_archive('Ex19_Shutil_01/backup arquivos python', 'zip', os.getcwd())