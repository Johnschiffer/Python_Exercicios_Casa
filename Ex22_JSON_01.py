# 4 principais comandos de uma API

import requests
from pprint import pprint

# GET

print('-'*50)

resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get.json())

print('-'*50)

# GET com id
resultado_get_id = resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_id.json())

print('-'*50)

# POST - Criar novo recurso
nova_tarefa = {'completed': False,
                'title': 'Estudando Python',
                'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
pprint(resultado_post.json())

print('-'*50)

# PUT - Alterar um recurso existente
tarefa_alterada = {'completed': False,
                'title': 'Estudando C++',
                'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2',tarefa_alterada)
pprint(resultado_put.json())


print('-'*50)


# DELETE - Excluir um recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())



