# Metodos de uma Classe
class Computador:
    def __init__(self, marca, memoria, placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video

    def ligar(self):
        print('Ligando Computador')

    def desligar(self):
        print('Desligando Computador')

    def dados_do_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria} de RAM e com placa de video {self.placa_video}')


computador1 = Computador('Asus', '8GB', 'NVIDIA')
computador1.ligar()
computador1.desligar()
computador1.dados_do_computador()