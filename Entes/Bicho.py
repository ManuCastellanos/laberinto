from Entes.Ente import Ente 
from State.Muerto import Muerto

class Bicho(Ente):
    # Constructor
    def __init__(self):
        super().__init__()

    def esBicho(self):
        return True
    
    def esPerezoso(self):
        return False
    
    def esAgresivo(self):
        return False
    
    def actua(self):
        self.modo.actua(self)
    
    def buscarEnemigo(self):
        self.juego.buscarPersonaje(self)
    
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def saMorio(self):
        self.estado = Muerto()
        print (self, "la ha roscao.")
        self.juego.bichoMuerto(self)
    
    def puedeActuar(self):
        self.modo.actua(self)
    
    def restarVida(self):
        self.vidas -= 1
        
    def atacar(self):
        self.juego.buscarPersonaje(self.posicion)
    
    # Metodos Caminar
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    # Como el toString de Java
    def __str__(self):
        return "Bicho " + str(self.modo)
    
