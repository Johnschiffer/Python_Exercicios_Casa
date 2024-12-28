# nome = parametro comum
# *args = quantidade ilimitada de argumentos posicionais
# **kwargs = quantidade ilimitada de argumentos nomeados

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)

    for arg in args:
        print(arg)

    for kwarg in kwargs.values():
        print(kwarg)


fazer_calculo('Jeff', 4, 5, 6, 7, 8, a=1, b=2, c=3, d=4)
             # nome  - *args         - **kwargs