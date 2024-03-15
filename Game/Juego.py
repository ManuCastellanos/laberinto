import threading
from Bicho import Bicho
from EM.Cont.Habitacion import Habitacion
from EM.Cont.Laberinto import Laberinto
from EM.Hoj.Deco.Bomba import Bomba
from EM.Pare.Pared import Pared
from EM.Pare.ParedBomba import ParedBomba
from EM.Puerta import Puerta
from Mode.Agresivo import Agresivo
from Mode.Perezoso import Perezoso
from Orientation.Norte import Norte
from Orientation.Sur import Sur
from Orientation.Este import Este
from Orientation.Oeste import Oeste


class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.hilos = {}
    
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
    
    def fabricarPuerta(self):
        return Puerta()
    
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
    

    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarOeste())
        
        hab.ponerEn(Norte(), self.fabricarPared())
        hab.ponerEn(Este(), self.fabricarPared())
        hab.ponerEn(Sur(), self.fabricarPared())    
        hab.ponerEn(Oeste(), self.fabricarPared())
        
        return hab
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarLaberinto2Habitaciones(self):
        print("\n Laberinto de 2 habitaciones ")
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        
        hab1.norte = Pared()
        hab1.este = Pared()
        hab1.oeste = Pared()
        
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()
        
        puerta = Puerta(hab1, hab2)
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    def fabricarLaberinto2Habitaciones2BombasFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = Puerta(hab1, hab2)
        
        hab1.norte = self.fabricarPared()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        
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
    
    def fabricarLaberinto2HabitacionesFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuertaLado1(hab1, hab2)
        
        hab1.ponerEn(Sur(), puerta)
        hab2.ponerEn(Norte(), puerta)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    def fabricarLaberinto2HabitacionesFMD(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuertaLado1(hab1, hab2)
        
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
    
    def fabricarLaberinto4Habitaciones4BichosFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        
        p12 = self.fabricarPuertaLado1(hab1, hab2)
        p13 = self.fabricarPuertaLado1(hab1, hab3)
        p34 = self.fabricarPuertaLado1(hab3, hab4)
        p24 = self.fabricarPuertaLado1(hab2, hab4)
        
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

    
    def fabricarPuertaLado1(self, unaHab, otraHab):
        puerta = Puerta(unaHab, otraHab)
        return puerta
    
    #Gestion de Bichos
    
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

    def __str__ (self):
        bichetes=""
        for bicho in self.bichos:
            bichetes+=str(bicho)+"\n"
            
        return f"\n Juego:\n {self.laberinto} \nBichos: \n{bichetes} \n" 