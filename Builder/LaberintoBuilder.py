from Bicho import Bicho
from EM.Cont.Habitacion import Habitacion
from EM.Cont.Laberinto import Laberinto
from EM.Hoj.Deco.Bomba import Bomba
from EM.Pare.Pared import Pared
from EM.Pare.ParedBomba import ParedBomba
from EM.Puerta import Puerta
from Game.Juego import Juego
from Mode.Agresivo import Agresivo
from Mode.Perezoso import Perezoso
from Orientation.Norte import Norte
from Orientation.Sur import Sur
from Orientation.Este import Este
from Orientation.Oeste import Oeste

class LaberintoBuilder():
    def __init__(self):
        self.juego = None
        self.laberinto = None
    
    def getJuego(self):
        return self.juego
    
    def fabricarJuego(self):
        self.juego = Juego()
        self.juego.laberinto = self.laberinto
        return self.juego
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarParedBomba(self):
        return ParedBomba()
    
    def fabricarPuerta(self, habitacion1, habitacion2):
        return Puerta(habitacion1, habitacion2)
    
    def fabricarPuertaBuilder(self, hab1, unaOr, hab2, otraOr):
        hab1= self.laberinto.obtenerHabitacion(hab1)
        hab2= self.laberinto.obtenerHabitacion(hab2)
        
        cad1= getattr(self,'fabricar'+unaOr)()
        cad2= getattr(self,'fabricar'+otraOr)()
        
        hab1.ponerEn(cad1, self.fabricarPuerta(hab1, hab2))
        hab2.ponerEn(cad2, self.fabricarPuerta(hab2, hab1))
        
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 5
        bicho.poder = 2
        bicho.posicion = self.juego.laberinto.obtenerHabitacion(unaHab)
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 2
        bicho.poder = 0
        bicho.posicion = self.juego.laberinto.obtenerHabitacion(unaHab)
        return bicho
     
    def fabricarHabitacion(self, num):
        hab= Habitacion(num)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarOeste())
        
        hab.ponerEn(Norte(), self.fabricarPared())
        hab.ponerEn(Este(), self.fabricarPared())
        hab.ponerEn(Sur(), self.fabricarPared())
        hab.ponerEn(Oeste(), self.fabricarPared())
        
        self.laberinto.agregarHabitacion(hab)
        
        return hab
    
    def fabricarBicho(self, modo, vidas, poder, posicion):
        bicho = Bicho()
        bicho.modo = modo
        bicho.vidas = vidas
        bicho.poder = poder
        bicho.posicion = posicion
        return bicho
    