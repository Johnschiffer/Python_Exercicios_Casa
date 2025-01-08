# Classe
class Computador:
    def __init__(self, marca, memoria, placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video


computador1 = Computador('Asus', '8GB', 'NVIDIA')
print(computador1.marca, computador1.memoria, computador1.placa_video)