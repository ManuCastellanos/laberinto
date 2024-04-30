import threading
from Bridge.Cuadrado import Cuadrado
from Entes.Bicho import Bicho
from EM.Container.Habitacion import Habitacion
from EM.Container.Laberinto import Laberinto
from EM.Hoj.Decorator.Bomba import Bomba
from EM.Pare.Pared import Pared
from EM.Pare.ParedBomba import ParedBomba
from EM.Puerta import Puerta
from Mode.BichosM.Agresivo import Agresivo
from Mode.BichosM.Perezoso import Perezoso
from Orientation.Norte import Norte
from Orientation.Sur import Sur
from Orientation.Este import Este
from Orientation.Oeste import Oeste

class LaberintoAFactory():
    def __init__(self):
        pass
    
    #Abstract Factory
    
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
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBicho(self, modo, vidas, poder, posicion):
        bicho = Bicho()
        bicho.modo = modo
        bicho.vidas = vidas
        bicho.poder = poder
        bicho.posicion = posicion
        return bicho
        
    def fabricarBichoAgresivo(self, unaHab):
        bicho = self.fabricarBicho(self.fabricarModoAgresivo(), 5, 2, unaHab)
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = self.fabricarBicho(self.fabricarModoPerezoso(), 2, 0, unaHab)
        return bicho
     
    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        hab.forma= self.fabricarForma()
        hab.forma.unNum= unNum
        
        hab.forma.agregarOrientacion(self.fabricarNorte())
        hab.forma.agregarOrientacion(self.fabricarEste())
        hab.forma.agregarOrientacion(self.fabricarSur())
        hab.forma.agregarOrientacion(self.fabricarOeste())
        
        hab.forma.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        hab.forma.ponerElemento(self.fabricarEste(), self.fabricarPared())
        hab.forma.ponerElemento(self.fabricarSur(), self.fabricarPared())    
        hab.forma.ponerElemento(self.fabricarOeste(), self.fabricarPared())
    
        return hab
    
    def fabricarArmario(self, unNum):
        arm= Armario(unNum)
        arm.forma= self.fabricarForma()
        
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarSur())
        arm.agregarOrientacion(self.fabricarOeste())
        
        arm.forma.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarEste(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarSur(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarOeste(), self.fabricarPared())
        
        return arm
    def fabricarForma(self):
        return Cuadrado()