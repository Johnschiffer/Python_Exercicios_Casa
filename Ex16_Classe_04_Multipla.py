# Herança Multipla
# Metodos com o mesmo nome dentro de classes, sempre utilizara o primeiro

class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá sou uma pessoa, vamos ao evento?')

class Profissional:
    nome = 'Sou uma profissional'

    def convidar(self):
        print('Olá sou uma profissional, vamos ao evento?')

class AtorProfissional(Pessoa, Profissional):
    pass

ator_profissional = AtorProfissional()
ator_profissional.convidar()
