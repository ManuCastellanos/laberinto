from Builder.LaberintoBuilder import LaberintoBuilder
import json

class Director():
    def __init__(self):
        self.builder = None
        self.director = None
    
    def iniBuilder(self):
        self.builder = LaberintoBuilder()
    
    def getJuego(self):
        return self.builder.juego
    
    def crearJuego(self):
        self.builder.fabricarJuego()
        
        for bicho in self.director['bichos']:
            if bicho['modo'] == 'agresivo':
                self.builder.juego.agregarBicho(self.builder.fabricarBichoAgresivo(bicho['hab']))
            else:
                self.builder.juego.agregarBicho(self.builder.fabricarBichoPerezoso(bicho['hab']))
    
    def crearLaberintoRecursivo(self, laberinto, root):
        if laberinto['tipo'] == 'habitacion':
            obj=self.builder.fabricarHabitacion(laberinto['num'])
            
        #hijos = laberinto.get('hijos', [])
        #for hijo in hijos:
        #    self.crearLaberintoRecursivo(hijo, obj)
        
    def crearLaberinto(self):
        self.builder.fabricarLaberinto()
        for laberinto in self.director['laberinto']:
            self.crearLaberintoRecursivo(laberinto, 'root')
        for puerta in self.director['puertas']:
            self.builder.fabricarPuertaBuilder(puerta[0], puerta[1], puerta[2], puerta[3])
    
    def verConfig(self, ruta):
        self.director = json.load(open(ruta,'r'))
        
    def procesar(self, ruta):
        self.verConfig(ruta)
        self.iniBuilder()
        self.crearLaberinto()
        self.crearJuego()
