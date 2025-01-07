# Ordene a lista em ordem descrecente por valor

from operator import itemgetter

produtos = [
    ('Tripe', 300),
    ('Câmera', 1700),
    ('Iluminação', 200)
]

produtos.sort(key=itemgetter(1), reverse=True)
print(produtos)