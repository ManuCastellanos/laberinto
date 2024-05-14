from colorama import Fore, Style, init
from Entes.Ente import Ente
from Items.Inventario import Inventario
from State.Muerto import Muerto

class Personaje(Ente):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.inventario = Inventario()
        self.compi = None
        
    
    def esPersonaje(self):
        return True
    
    def obtenerComandos(self, prota):
        return self.posicion.obtenerComandos(prota)
    
    def cogerItem(self, item):
        self.inventario.agregarItem(item)
        print("Se ha cogido ", item)
    
    def soltarItem(self, item):
        self.inventario.quitarItem(item)
        print("Se ha soltado ", item)
    
    def abrirInventario(self):
        self.inventario.abrirInventario()
        
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def saMorio(self):
        init()
        self.estado = Muerto()
        print (Fore.RED + str(self), "la ha roscao." + Style.RESET_ALL)
        self.juego.personajeMuerto(self)
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def __str__(self):
        return str(self.nombre) + " en " +  str(self.posicion.num)