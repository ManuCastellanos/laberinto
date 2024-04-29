from Entes.Ente import Ente
import State.Muerto as Muerto

class Personaje(Ente):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        
    
    def esPersonaje(self):
        return True
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def saMorio(self):
        self.estado = Muerto()
        print (self, "la ha roscao.")
        self.juego.personajeMuerto(self)
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    def __str__(self):
        return str(self.nombre)#+ str(self.modo)