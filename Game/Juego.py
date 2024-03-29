import threading
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
from Entes.Personaje import Personaje
from Mode.PersonajeM.Normal import Normal
from EM.Container.Armario import Armario

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.hilos = {}
        self.prota= None
        
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
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarSur())
        arm.agregarOrientacion(self.fabricarOeste())
        
        arm.ponerEn(self.fabricarNorte(), self.fabricarPared())
        arm.ponerEn(self.fabricarEste(), self.fabricarPared())
        arm.ponerEn(self.fabricarSur(), self.fabricarPared())
        arm.ponerEn(self.fabricarOeste(), self.fabricarPared())
        
        return arm
    
    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarOeste())
        
        hab.ponerEn(self.fabricarNorte(), self.fabricarPared())
        hab.ponerEn(self.fabricarEste(), self.fabricarPared())
        hab.ponerEn(self.fabricarSur(), self.fabricarPared())    
        hab.ponerEn(self.fabricarOeste(), self.fabricarPared())
        
        return hab
    
    def fabricarPuerta(self, unaHab, otraHab):
        puerta = Puerta(unaHab, otraHab)
        return puerta
    
    #Gestion de Bichos
    def agregarProta(self,unProta):
       self.prota= unProta
        
    def fabricarPersonajeNormal(self):
        self.prota= Personaje()
        self.prota.modo = Normal()
        self.prota.vidas = 5
        self.prota.poder = 2
        self.prota.nombre = "Imbécil" #input("Introduce el nombre del personaje: ")
        self.laberinto.entrar(self.prota)
        return self.prota
        
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print("No existe ese bicho")

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
            unaPuerta.abrir()
    
    def cerrarPuerta(self, unaPuerta):
        if unaPuerta.esPuerta():
            unaPuerta.cerrar() 
    
    def abrirPuertas(self):
        self.laberinto.recorrer(self.abrirPuerta)
    
    def cerrarPuertas(self):
        self.laberinto.recorrer(self.cerrarPuerta)
    
    def lanzarHilo(self, unBicho):
        def proceso_target():
            while True:
                unBicho.actua()

        proceso = threading.Thread(target=proceso_target)
        proceso.start()
        self.hilos[unBicho] = proceso

    def terminarHilo(self, unBicho):
        proceso = self.hilos.get(unBicho)
        if proceso:
            proceso.terminate()
            
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
        
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
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
        
        hab1.ponerEn(self.fabricarSur(), puerta)
        hab2.ponerEn(self.fabricarNorte(), puerta)
        
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
        
        hab1.norte = self.fabricarPared()
        hab1.este = bm1
        hab1.oeste = self.fabricarPared()
        
        bm2 = self.fabricarBomba()
        bm2.em = self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.este = bm2
        hab2.oeste = self.fabricarPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
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
        
        hab1.ponerEn(self.fabricarSur(), p12)
        hab2.ponerEn(self.fabricarNorte(), p12)
        
        hab1.ponerEn(self.fabricarEste(), p13)
        hab3.ponerEn(self.fabricarOeste(), p13)
        
        hab2.ponerEn(self.fabricarEste(), p24)
        hab4.ponerEn(self.fabricarOeste(), p24)
        
        hab3.ponerEn(self.fabricarSur(), p34)
        hab4.ponerEn(self.fabricarNorte(), p34)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))

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
        
        hab1.ponerEn(unAF.fabricarSur(), p12)
        hab2.ponerEn(unAF.fabricarNorte(), p12)
        
        hab1.ponerEn(unAF.fabricarEste(), p13)
        hab3.ponerEn(unAF.fabricarOeste(), p13)
        
        hab2.ponerEn(unAF.fabricarEste(), p24)
        hab4.ponerEn(unAF.fabricarOeste(), p24)
        
        hab3.ponerEn(unAF.fabricarSur(), p34)
        hab4.ponerEn(unAF.fabricarNorte(), p34)
        
        hab1.ponerEn(unAF.fabricarNorte(), unAF.fabricarParedBomba())
        hab2.ponerEn(unAF.fabricarSur(), unAF.fabricarParedBomba())
        hab3.ponerEn(unAF.fabricarEste(), unAF.fabricarParedBomba())
        hab4.ponerEn(unAF.fabricarOeste(), unAF.fabricarParedBomba())
        
        self.agregarBicho(unAF.fabricarBichoAgresivo(hab1))
        self.agregarBicho(unAF.fabricarBichoAgresivo(hab3))
        self.agregarBicho(unAF.fabricarBichoPerezoso(hab2))
        self.agregarBicho(unAF.fabricarBichoPerezoso(hab4))
        
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
    
    def fabricarLaberintoPersonaje(self):
        
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        
        p12 = self.fabricarPuerta(hab1, hab2)
        p13 = self.fabricarPuerta(hab1, hab3)
        p34 = self.fabricarPuerta(hab3, hab4)
        p24 = self.fabricarPuerta(hab2, hab4)
        
        hab1.ponerEn(self.fabricarSur(), p12)
        hab2.ponerEn(self.fabricarNorte(), p12)
        
        hab1.ponerEn(self.fabricarEste(), p13)
        hab3.ponerEn(self.fabricarOeste(), p13)
        
        hab2.ponerEn(self.fabricarEste(), p24)
        hab4.ponerEn(self.fabricarOeste(), p24)
        
        hab3.ponerEn(self.fabricarSur(), p34)
        hab4.ponerEn(self.fabricarNorte(), p34)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        
        arm1= self.fabricarArmario(1)
        
        parm= self.fabricarPuerta(hab1, arm1)
        arm1.ponerEn(self.fabricarSur(), parm)
        
        hab1.agregarHijo(arm1)
        
        self.agregarProta(self.fabricarPersonajeNormal())
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))
          
    def __str__ (self):
        bichetes=""
        for bicho in self.bichos:
            bichetes+=str(bicho)+"\n"
            
        return f"\n Juego:\n {self.laberinto} \nBichos: \n{bichetes} \n Protagonista: {self.prota} \n" 