# Classe Herança

# Classe PAI
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels
    
    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca}, qualidade {self.megapixels} Megapixels')


# Classe FILHO
class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_cameras):
        super().__init__(marca, megapixels) # Utiliza os mesmos argumentos da Classe Pai
        # Acrescenta + um argumento
        self.quantidade_cameras = quantidade_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    def tirar_foto(self, camera_utilizada):
        print(f'Foto tirada com a camera {self.marca}'
              f'com a qualidade {self.megapixels} Megapixels'
              f'Utilizando a camera {camera_utilizada}')
        
# Classe FILHO 2
class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_max_gravacao):
        super().__init__(marca, megapixels) # Utiliza os mesmos argumentos da Classe Pai
        # Acrescenta + um argumento
        self.horas_max_gravacao = horas_max_gravacao

    def rotacionar_camera(self, direcao):
        print(f'Rotacionando a camera para {direcao}')


camera_seguranca = CameraSeguranca('Sony', '5MP', 10)
camera_seguranca.rotacionar_camera('Direita')
