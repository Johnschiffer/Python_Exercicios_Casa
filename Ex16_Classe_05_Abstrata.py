# Classes abstratas
# Cria um esqueleto que dever ser implementado na classe que a herda

from abc import ABC, abstractclassmethod

class Monitor(ABC):
    def aumentar_claridade(self, pontos):
        pass

    def diminuiir_claridade(self, pontos):
        pass

class MoniutorFullHD(Monitor):
    def aumentar_claridade(self, pontos):
        print(f'Aumentando claridade em {pontos} pontos')

    def diminuiir_claridade(self, pontos):
        print(f'diminuir claridade em {pontos} pontos')

monitor = MoniutorFullHD()
monitor.aumentar_claridade(10)
monitor.diminuiir_claridade(5)