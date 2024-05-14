import copy
import threading

from colorama import init
from Comandos.Abrir import Abrir
from EM.Container.Cornucopia import Cornucopia
from Entes.Bicho import Bicho
from EM.Container.Habitacion import Habitacion
from EM.Container.Laberinto import Laberinto
from EM.Hoj.Decorator.Bomba import Bomba
from EM.Pare.Pared import Pared
from EM.Pare.ParedBomba import ParedBomba
from EM.Puerta import Puerta
from Entes.Compañero import Compañero
from Fases.Final import Final
from Fases.Inical import Inicial
from Fases.Jugando import Jugando
from Items.Agua import Agua
from Items.Comida import Comida
from Mode.BichosM.Agresivo import Agresivo
from Mode.BichosM.Perezoso import Perezoso
from Orientation.Norte import Norte
from Orientation.Sur import Sur
from Orientation.Este import Este
from Orientation.Oeste import Oeste
from Entes.Personaje import Personaje
from Mode.PersonajeM.Normal import Normal
from EM.Container.Armario import Armario
from Bridge.Cuadrado import Cuadrado

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.compañeros = []
        self.hilos = dict()
        self.prototype = None
        self.personaje= None
        self.fase= Inicial()
        
    # Factory Method
    
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

    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 2
        bicho.posicion = unaHab
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 2
        bicho.poder = 0
        bicho.posicion = unaHab
        return bicho
    
    def fabricarBomba(self):
        return Bomba()
    
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
    
    def fabricarPuerta(self, unaHab, otraHab):
        puerta = Puerta(unaHab, otraHab)
        puerta.agregarComando(Abrir(),puerta)
        return puerta
    
    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarComida(self):
        return Comida()
    
    def fabricarAgua(self):
        return Agua()
    
    def fabricarCornucopia(self, unCont):
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
        
        corn.items = [self.fabricarComida(), self.fabricarAgua()]
        
        unCont.agregarHijo(corn)
        
        return corn
    
    #Gestion de Bichos        
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)
        unBicho.juego = self
        
    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print("No existe ese bicho")

    # Gestion de compis
    
    def agregarCompañero(self, unCompañero):
        self.compañeros.append(unCompañero)
        unCompañero.juego = self
    
    def activarBomba(self, unEM):
        if unEM.esBomba():
            unEM.activar()
    
    def desactivarBomba(self, unEM):
        if unEM.esBomba():
            unEM.desactivar()
    
    def activarBombas(self):
        self.laberinto.recorrer(self.activarBomba)
    
    def desactivarBombas(self):
        self.laberinto.recorrer(self.desactivarBomba)
    
    def abrirPuerta(self, unaPuerta):
        if unaPuerta.esPuerta():
            unaPuerta.abrir(None)
    
    def cerrarPuerta(self, unaPuerta):
        if unaPuerta.esPuerta():
            unaPuerta.cerrar(None) 
    
    def abrirPuertas(self):
        self.laberinto.recorrer(self.abrirPuerta)
    
    def cerrarPuertas(self):
        self.laberinto.recorrer(self.cerrarPuerta)
    
    ## *********** HILOS ***********
    def agregarHilo(self,unHilo,unEnte):
        self.hilos[unEnte] = unHilo
    
    def lanzoBichos(self):
        for bicho in self.bichos:
            if bicho in self.hilos:
                print ("Hilo de ", bicho, "en ejecución")
            else:
                self.lanzarHilo(bicho)
                
    def lanzarHilo(self, unEnte):
        if isinstance(unEnte,Bicho):
            hilo = threading.Thread(target=lambda: self.hiloBicho(unEnte))
            self.agregarHilo(hilo, unEnte)
            
        elif isinstance(unEnte,Compañero):
            hilo = threading.Thread(target=lambda: self.hiloCompi(unEnte))
            self.agregarHilo(hilo, unEnte)
        hilo.start()

    def hiloBicho(self, unBicho):
        while unBicho.estaVivo():
            unBicho.actua()
    
    def allBichosMoridos(self):
        result = None
        for bicho in self.bichos:
            if bicho.estaVivo():
                result = bicho
        if result is None:
            return True
        result = None
        return False
    
    def terminarHiloBicho(self):
        for bicho in self.bichos [:]:
           self.terminarHilo(bicho)
    
    def hiloCompi(self, unCompi):
        while unCompi.estaVivo():
            unCompi.actuaC(unCompi,self.personaje) 
    
    def terminarHiloCompi(self):
        for compi in self.compañeros:
            self.terminarHilo(compi)
            
    def lanzoCompis(self):
        for compi in self.compañeros:
            if compi in self.hilos:
                print ("Hilo de ", compi, "en ejecución")
            else:
                self.lanzarHilo(compi)
    
    
    def terminarHilo(self, unEnte):
        unEnte.saMorio()
  
    def bichoMuerto (self,unBicho):
        init()
        self.eliminarBicho(unBicho)
        if self.allBichosMoridos():
            if self.personaje.estaVivo():
                self.finJuego()
                print("HA GANADO " + str(self.personaje.nombre))
            else:   
             self.finJuego()
    
    def personajeMuerto(self,unProta):
        print("TE ACABAN DE MATAR " + str(self.personaje.nombre))
        cadena=""
        for bicho in self.bichos:
            cadena+=str(bicho)+"\n"
        
        print("HAN GANADO LOS BICHOS: \n"+cadena)
        self.finJuego()
        
    def finJuego(self):
        self.fase= Final()
        self.terminarHiloBicho()
        self.terminarHiloCompi()
        
        
    ## ********* BUSCAR *********
    
    def buscarPersonaje(self,unBicho):
        pos = self.personaje.posicion
            
        if unBicho.posicion == pos:
            return self.personaje
        
        return None
    
    def buscarBicho(self):
        pos= self.personaje.posicion
        for bicho in self.bichos:
            if bicho.posicion == pos:
                return bicho
    
    def buscarCompi(self):
        pos= self.personaje.posicion
        for compi in self.compañeros:
            if compi.posicion == pos:
                return compi
            
    def buscarCompiEn(self, unaHab):
        for compi in self.compañeros:
            if compi.posicion == unaHab:
                print( self.personaje.nombre + " tiene a " + compi.__str__())
                return compi
        return None
    
    def clonarLaberinto(self):
        self.prototype = copy.deepcopy(self.laberinto)
        self.prototype.num = self.laberinto.num + 1
        return self.prototype
    
    def puedeIniProta(self, unProta):
        self.personaje= unProta
        self.personaje.juego = self
        self.personaje.vidas = 15
        self.personaje.poder = 2
        self.personaje.posicion = self.laberinto.obtenerHabitacion(1)
        self.personaje.compi=self.buscarCompiEn(self.personaje.posicion)
    
    def iniProta(self, unProta):
        self.fase.agregarIniProta(unProta, self)
        self.fase= Jugando()
    
    #-------------LABERINTOS----------------
            
    def fabricarLaberinto(self):
        return Laberinto()
    
    #-------------Laberinto con 2 habitaciones----------------
    def fabricarLaberinto2Habitaciones(self):
        print("\n Laberinto de 2 habitaciones ")
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        
        hab1.norte = Pared()
        hab1.este = Pared()
        hab1.oeste = Pared()
        
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()
        
        puerta = Puerta(hab1, hab2)
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = Laberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    #-------------Laberinto con 2 habitaciones y 2 bombas Factory Method----------------
    def fabricarLaberinto2Habitaciones2BombasFM(self): #????????
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)
        
        hab1.forma.norte = self.fabricarPared()
        hab1.forma.oeste = self.fabricarPared()
        hab1.forma.este = self.fabricarPared()
        
        hab2.forma.sur = self.fabricarPared()
        hab2.forma.este = self.fabricarPared()
        hab2.forma.oeste = self.fabricarPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.forma.sur = puerta
        hab2.forma.norte = puerta
        
        bm1 = self.fabricarBomba()
        bm2 = self.fabricarBomba()
        
        hab1.agregarHijo(bm1)
        hab2.agregarHijo(bm2)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    #-------------Laberinto con 2 habitaciones Factory Method----------------
    def fabricarLaberinto2HabitacionesFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        
        puerta = self.fabricarPuerta(hab1, hab2)
        
        hab1.ponerElementoEn(self.fabricarNorte(), puerta)
        hab2.ponerElementoEn(self.fabricarSur(), puerta)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    #-------------Laberinto con 2 habitaciones y 2 bombas Factory Method Decorator----------------
    def fabricarLaberinto2HabitacionesFMD(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)
        
        bm1 = self.fabricarBomba()
        bm1.em = self.fabricarPared()
        hab1.forma.este = bm1
        
        bm2 = self.fabricarBomba()
        hab2.forma.este = bm2

        hab1.ponerElementoEn(self.fabricarNorte(), puerta)
        hab2.ponerElementoEn(self.fabricarSur(), puerta)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    #-------------Laberinto con 4 habitaciones y 4 bichos----------------
    def fabricarLaberinto4Habitaciones4BichosFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        
        p12 = self.fabricarPuerta(hab1, hab2)
        p13 = self.fabricarPuerta(hab1, hab3)
        p34 = self.fabricarPuerta(hab3, hab4)
        p24 = self.fabricarPuerta(hab2, hab4)
        
        hab1.forma.ponerElemento(self.fabricarSur(), p12)
        hab2.forma.ponerElemento(self.fabricarNorte(), p12)
        
        hab1.forma.ponerElemento(self.fabricarEste(), p13)
        hab3.forma.ponerElemento(self.fabricarOeste(), p13)
        
        hab2.forma.ponerElemento(self.fabricarEste(), p24)
        hab4.forma.ponerElemento(self.fabricarOeste(), p24)
        
        hab3.forma.ponerElemento(self.fabricarSur(), p34)
        hab4.forma.ponerElemento(self.fabricarNorte(), p34)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))

        self.iniProta("Manuel")
        
    # -------------Laberinto con 4 habitaciones, 4 Bombas y 4 bichos Abstract Factory----------------
    def fabricarLaberinto4Hab4Bomb4BichosAF(self,unAF):
        print("\n Laberinto de 4 habitaciones, 4 Bombas y 4 bichos ")
        self.laberinto=unAF.fabricarLaberinto()
        hab1 = unAF.fabricarHabitacion(1)
        hab2 = unAF.fabricarHabitacion(2)
        hab3 = unAF.fabricarHabitacion(3)
        hab4 = unAF.fabricarHabitacion(4)
        
        p12 = unAF.fabricarPuerta(hab1, hab2)
        p13 = unAF.fabricarPuerta(hab1, hab3)
        p34 = unAF.fabricarPuerta(hab3, hab4)
        p24 = unAF.fabricarPuerta(hab2, hab4)
        
        hab1.forma.ponerElemento(unAF.fabricarSur(), p12)
        hab2.forma.ponerElemento(unAF.fabricarNorte(), p12)
        
        hab1.forma.ponerElemento(unAF.fabricarEste(), p13)
        hab3.forma.ponerElemento(unAF.fabricarOeste(), p13)
        
        hab2.forma.ponerElemento(unAF.fabricarEste(), p24)
        hab4.forma.ponerElemento(unAF.fabricarOeste(), p24)
        
        hab3.forma.ponerElemento(unAF.fabricarSur(), p34)
        hab4.forma.ponerElemento(unAF.fabricarNorte(), p34)
        
        hab1.forma.ponerElemento(unAF.fabricarNorte(), unAF.fabricarParedBomba())
        hab2.forma.ponerElemento(unAF.fabricarSur(), unAF.fabricarParedBomba())
        hab3.forma.ponerElemento(unAF.fabricarEste(), unAF.fabricarParedBomba())
        hab4.forma.ponerElemento(unAF.fabricarSur(), unAF.fabricarParedBomba())
        
        self.agregarBicho(unAF.fabricarBichoAgresivo(hab1))
        self.agregarBicho(unAF.fabricarBichoAgresivo(hab3))
        self.agregarBicho(unAF.fabricarBichoPerezoso(hab2))
        self.agregarBicho(unAF.fabricarBichoPerezoso(hab4))
        
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
    
    #************** Laberinto con 4 habitaciones, 4 bichos, 2 bombas y un personaje **************
    def fabricarLaberintoPersonaje(self):
        
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        
        p12 = self.fabricarPuerta(hab1, hab2)
        p13 = self.fabricarPuerta(hab1, hab3)
        p34 = self.fabricarPuerta(hab3, hab4)
        p24 = self.fabricarPuerta(hab2, hab4)
        
        hab1.forma.ponerElemento(self.fabricarSur(), p12)
        hab2.forma.ponerElemento(self.fabricarNorte(), p12)
        
        hab1.forma.ponerElemento(self.fabricarEste(), p13)
        hab3.forma.ponerElemento(self.fabricarOeste(), p13)
        
        hab2.forma.ponerElemento(self.fabricarEste(), p24)
        hab4.forma.ponerElemento(self.fabricarOeste(), p24)
        
        hab3.forma.ponerElemento(self.fabricarSur(), p34)
        hab4.forma.ponerElemento(self.fabricarNorte(), p34)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        
        arm1= self.fabricarArmario(1)
        
        parm= self.fabricarPuerta(hab1, arm1)
        arm1.forma.ponerElemento(self.fabricarSur(), parm)
        
        hab1.agregarHijo(arm1)
        
        self.iniProta("Imbécil")
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))
          
    def __str__ (self):
        bichetes=""
        compis=""
        
        for bicho in self.bichos:
            bichetes+=str(bicho)+"\n"
        
        for compi in self.compañeros:
            compis+=str(compi)+"\n"
            
        return f"\n Juego:\n {self.laberinto} \nBichos:\n{bichetes} \nProtagonista: {self.personaje} \nCompis: \n{compis}" 