import os


# COMO CRIAR E MODIFICAR ARQUIVOS:
# 'w' -> Usado somente para escrever
# 'a' -> Usado para acrescentar
# 'r' -> Usado somente para ler 
# 'r+'-> Usado para ler e escrever

frutas = ['Manga', 'Maca', 'Morango', 'Banana']
cores = ['Vermelho', 'Azul', 'Amarelo', 'Roxo']
linguagens = ['Python', 'C++', 'C#', 'Java', 'C']

# Crie um arquivo frutas.txt e insira dentro dele todos as frutas da lista
with open('Ex18_Arquivos_04_Criar_Salvar_Editar/frutas.txt', 'w', newline ='') as arquivo:
    for fruta in frutas:
        arquivo.write(str(fruta) + os.linesep)


# Sem apagar os dados de frutas.txt adicione todas as cores da lista cores
with open('Ex18_Arquivos_04_Criar_Salvar_Editar/frutas.txt', 'a', newline ='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + str(cor))


# Crie um novo arvquivo "Top 5 lingagens" e adicione cada linguagem em uma linha
with open('Ex18_Arquivos_04_Criar_Salvar_Editar/Top_Lingaguens.txt', 'w', newline ='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(str(linguagem) + os.linesep)
    print(linguagem)
