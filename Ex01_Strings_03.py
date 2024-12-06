teclado = 'Teclado'

print(teclado[-1]) # Acessa o último indice
print(teclado.index('l')) # Retorna o indice da letra desejada
print(teclado[teclado.index('l')]) # Encontra onde está a letra desejada e a retorna

# Acessando partes de uma string

link = 'facebook.com/johnschiffer'

print(link[0]) # Acessa o primeiro item da string
print(link[-1]) # Acessa o último indice
print(link[0:5]) # Onde iniciar [0], onde terminar [5] (não inclui o último indice)
print(link[0:]) # Onde iniciar [0], depois até o final
print(link[-5:]) # Vai até o final e volte [-5], depois até o final
print(link[5:]) # Iniciar no indicia [5], ir até o final
print(link[:-5]) # Inicia do [0] e vai até o -5 do final até o inicio