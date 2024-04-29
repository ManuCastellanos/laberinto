from Entes.Ente import Ente

class Personaje(Ente):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def esPersonaje(self):
        return True
    
    def __str__(self):
        return str(self.nombre)#+ str(self.modo)