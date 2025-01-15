import random  # Importa o módulo random para gerar números aleatórios.

class SimuladorDeDado:  # Define uma classe que representa o simulador de dado.
    def __init__(self):  # Método construtor, chamado quando a classe é instanciada.
        self.valor_minimo = 1  # Define o valor mínimo do dado como 1.
        self.valor_maximo = 6  # Define o valor máximo do dado como 6.
    
    def iniciar(self):  # Método principal que inicia o simulador.
        self.ImprimirNumeroAleatorioLimite()  # Chama o método para gerar e imprimir um número aleatório.
        self.PerguntarSeDeveRodarNovamente()  # Chama o método para perguntar ao usuário se deseja rodar novamente.

    def ImprimirNumeroAleatorioLimite(self):  # Método para gerar e imprimir o número aleatório.        
        print(f'Girando dado: ', (random.randint(self.valor_minimo, self.valor_maximo))) # Gera um número aleatório entre valor_minimo (1) e valor_maximo (6) e imprime no console.

    def PerguntarSeDeveRodarNovamente(self):  # Método que pergunta ao usuário se deseja rodar novamente.        
        rodar_novamente = input('Gostaria de rodar o dado novamente? (s/n): ') # Solicita ao usuário que informe se quer rodar o dado novamente.
        if rodar_novamente == 's':  # Caso o usuário digite 's', inicia o simulador novamente.
            self.iniciar()
        elif rodar_novamente == 'n':  # Caso o usuário digite 'n', encerra o programa.
            print('OK! Fechando programa.')
        else:  # Caso o usuário digite algo inválido, exibe uma mensagem e pergunta novamente.
            print('Favor digitar apenas \'s\' ou \'n\'')  # Exibe instruções para uma entrada válida.
            self.PerguntarSeDeveRodarNovamente()  # Chama o método novamente para solicitar a resposta correta.
    
# Cria uma instância da classe SimuladorDeDado.
simulador = SimuladorDeDado()

# Inicia o simulador chamando o método iniciar.
simulador.iniciar()