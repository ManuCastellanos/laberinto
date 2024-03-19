from Entes.Ente import Ente

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nombre = None

    def __str__(self):
        return str(self.nombre)#+ str(self.modo)