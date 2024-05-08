from Entes.Ente import Ente
import State.Muerto as Muerto

class Personaje(Ente):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.compi = None
        
    
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
        return str(self.nombre) + " en " +  str(self.posicion.num) + " tiene " + str(self.compi)#+ str(self.modo)