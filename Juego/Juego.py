import threading
from Bicho import Bicho
from EM.Contenedor import Habitacion, Laberinto
from EM.Hoja.Decorator import Bomba
from EM.Pared import Pared, ParedBomba
from EM.Puerta import Puerta
from Modo import Agresivo, Perezoso
from Orientacion import Orientacion, Norte, Este, Sur, Oeste


class Juego:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.bichos = []
        self.hilos = {}
    
    # Factory Method
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
    
    def fabricarEste(self):
        return Este.default()
    
    def fabricarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num = unNum
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(Este.default())
        hab.agregarOrientacion(Sur.default())
        hab.agregarOrientacion(Oeste.default())
        
        for each in hab.orientaciones:
            hab.ponerEn(each, self.fabricarPared())
        
        return hab
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarLaberinto2Habitaciones(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = Puerta()
        
        hab1.norte = Pared()
        hab1.este = Pared()
        hab1.oeste = Pared()
        
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
    def fabricarLaberinto2Habitaciones2BombasFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta()
        
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
        
        hab1.ponerEn(Sur.default(), puerta)
        hab2.ponerEn(Norte.default(), puerta)
        
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
        
        hab1.ponerEn(Sur.default(), p12)
        hab2.ponerEn(Norte.default(), p12)
        
        hab1.ponerEn(Este.default(), p13)
        hab3.ponerEn(Oeste.default(), p13)
        
        hab2.ponerEn(Este.default(), p24)
        hab4.ponerEn(Oeste.default(), p24)
        
        hab3.ponerEn(Sur.default(), p34)
        hab4.ponerEn(Norte.default(), p34)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))
    
    def fabricarNorte(self):
        return Norte.default()
    
    def fabricarOeste(self):
        return Oeste.default()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarPuertaLado1(self, unaHab, otraHab):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        return puerta
    
    def fabricarSur(self):
        return Sur.default()
    
    #Gestion de Bichos
    
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print("No existe ese bicho")

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