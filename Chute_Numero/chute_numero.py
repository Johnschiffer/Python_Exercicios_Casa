import random

class ChuteNumero:
    def __init__(self):
        self.num_random_min = 1
        self.num_random_max = 100
        self.num_random = random.randint(self.num_random_min, self.num_random_max)
    
    def iniciar(self):
        self.Pergunta_Chute()
    
    def Pergunta_Chute(self):
        resposta = int(input('Chute um numero: '))
        if resposta > self.num_random:
            print('Chute um valor menor!')
            self.iniciar()
        if resposta < self.num_random:
            print('Chute um valor maior!')
            self.iniciar()
        else:
            print('Você acertou!')

Inicia_jogo = ChuteNumero()
Inicia_jogo.iniciar()