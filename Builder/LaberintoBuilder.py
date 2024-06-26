from Bridge.Cuadrado import Cuadrado
from Comandos.Abrir import Abrir
from EM.Container.Armario import Armario
from EM.Container.Cornucopia import Cornucopia
from Entes.Bicho import Bicho
from EM.Container.Habitacion import Habitacion
from EM.Container.Laberinto import Laberinto
from EM.Hoj.Decorator.Bomba import Bomba
from EM.Pare.Pared import Pared
from EM.Pare.ParedBomba import ParedBomba
from EM.Puerta import Puerta
from Entes.Compañero import Compañero
from Game.Juego import Juego
from Items.Agua import Agua
from Items.Comida import Comida
from Mode.BichosM.Agresivo import Agresivo
from Mode.BichosM.Perezoso import Perezoso
from Mode.CompañeroM.Aura import Aura
from Mode.CompañeroM.Blitz import Blitz
from Orientation.Norte import Norte
from Orientation.Sur import Sur
from Orientation.Este import Este
from Orientation.Oeste import Oeste
from EM.Hoj.Tunel import Tunel

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
        puerta= Puerta(habitacion1, habitacion2)
        puerta.agregarComando(Abrir(),puerta)
        return puerta
    
    def fabricarPuertaBuilder(self, hab1, unaOr, hab2, otraOr):
        hab1= self.laberinto.obtenerHabitacion(hab1)
        hab2= self.laberinto.obtenerHabitacion(hab2)
        
        cad1= getattr(self,'fabricar'+unaOr)()
        cad2= getattr(self,'fabricar'+otraOr)()
        
        puerta= self.fabricarPuerta(hab1, hab2)
        
        hab1.forma.ponerElemento(cad1, puerta)
        hab2.forma.ponerElemento(cad2, puerta)
        
    
    def fabricarBombaHab(self,unCont):
        unCont.agregarHijo(self.fabricarBomba())
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarAura(self):
        return Aura()
    
    def fabricarBlitz(self):
        return Blitz()
    
    def fabricarCompañero(self, modo, vidas, poder, posicion):
        compi = Compañero()
        compi.modo = modo
        compi.vidas = vidas
        compi.poder = poder
        compi.posicion = posicion
        return compi
    
    def fabricarCompiAura(self,hab):
        compi= self.fabricarCompañero(self.fabricarAura(), 10, 0, self.laberinto.obtenerHabitacion(hab))
        return compi
    
    def fabricarCompiBlitz(self,hab):
        compi= self.fabricarCompañero(self.fabricarBlitz(), 8, 2, self.laberinto.obtenerHabitacion(hab))
        return compi
    
    def fabricarBicho(self, modo, vidas, poder, posicion):
        bicho = Bicho()
        bicho.modo = modo
        bicho.vidas = vidas
        bicho.poder = poder
        bicho.posicion = posicion
        return bicho
    
    def fabricarBichoAgresivo(self, unaHab):
        bicho = self.fabricarBicho(self.fabricarModoAgresivo(), 10, 3, self.laberinto.obtenerHabitacion(unaHab))
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = self.fabricarBicho(self.fabricarModoPerezoso(), 8, 2, self.laberinto.obtenerHabitacion(unaHab))
        return bicho
    
    def fabricarForma(self):
        return Cuadrado() 
    
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
        
        self.laberinto.agregarHabitacion(hab)
        
        return hab
    
    def fabricarArmarioEn(self, unCont):
        arm= Armario(unCont.num)
        arm.forma= self.fabricarForma()
        
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarSur())
        arm.agregarOrientacion(self.fabricarOeste())
        
        arm.forma.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarEste(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarSur(), self.fabricarPared())
        arm.forma.ponerElemento(self.fabricarOeste(), self.fabricarPared())
        
        unCont.agregarHijo(arm)
        
        return arm
    
    def fabricarTunel (self):
        tunel= Tunel()
        return tunel
    
    def fabricarTunelCont(self, unContenedor):
        unContenedor.agregarHijo(self.fabricarTunel())

    def fabricarComida(self):
        return Comida()
    
    def fabricarAgua(self):
        return Agua()
    
    def fabricarCornucopiaEn(self, unCont):
        corn= Cornucopia(unCont.num)
        corn.forma= self.fabricarForma()
        
        corn.agregarOrientacion(self.fabricarNorte())
        corn.agregarOrientacion(self.fabricarEste())
        corn.agregarOrientacion(self.fabricarSur())
        corn.agregarOrientacion(self.fabricarOeste())
        
        corn.forma.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        corn.forma.ponerElemento(self.fabricarEste(), self.fabricarPared())
        corn.forma.ponerElemento(self.fabricarSur(), self.fabricarPared())
        corn.forma.ponerElemento(self.fabricarOeste(), self.fabricarPared())
        
        puertaCorn = self.fabricarPuerta(corn, unCont)
        corn.forma.ponerElemento(self.fabricarOeste(), puertaCorn)

        corn.agregarItem(self.fabricarComida())
        corn.agregarItem(self.fabricarAgua())
        
        unCont.agregarHijo(corn)
        
        return corn
