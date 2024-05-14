from colorama import Fore, Style, init
from Entes.Ente import Ente 
from State.Muerto import Muerto

class Bicho(Ente):
    # Constructor
    def __init__(self):
        super().__init__()

    def esBicho(self):
        return True
    
    def esEnemigo(self):
        return True
    
    def esPerezoso(self):
        return False
    
    def esAgresivo(self):
        return False
    
    def actua(self):
        self.modo.actua(self)
    
    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)
    
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def saMorio(self):
        init()
        self.estado = Muerto()
        print (Fore.RED+str(self), "la ha roscao."+ Style.RESET_ALL)
        self.juego.bichoMuerto(self)
    
    def puedeActuar(self):
        self.modo.actua(self)
    
    def restarVida(self):
        self.vidas -= 1
        
    
    # Metodos Caminar
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    # Como el toString de Java
    def __str__(self):
        return "Bicho " + str(self.modo)
    
