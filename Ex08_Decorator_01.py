from datetime import datetime

def decorator(funcao):
    def hora_antes():
        print('Hora antes', datetime.now())

        funcao()

        print('Hora depois', datetime.now())
    return hora_antes

def parabenizar():
    print('Parabens!')

resultado = decorator(parabenizar)
resultado()