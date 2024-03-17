from Builder.LaberintoBuilder import LaberintoBuilder
import json

class Director():
    def __init__(self): 
        self.builder = None #LaberintoBuilder()
        self.director = None #Aquí cargo la información del JSON 
    
    def iniBuilder(self): #Inicializa el builder
        self.builder = LaberintoBuilder()
    
    def getJuego(self): #Devuelve el juego
        return self.builder.juego
    
    def crearJuego(self): #Crea el juego
        self.builder.fabricarJuego()
        
        for bicho in self.director['bichos']: #Agrega los bichos al juego
            if bicho['modo'] == 'agresivo':
                self.builder.juego.agregarBicho(self.builder.fabricarBichoAgresivo(bicho['hab']))
            else:
                self.builder.juego.agregarBicho(self.builder.fabricarBichoPerezoso(bicho['hab']))
    
    def crearLaberintoRecursivo(self, laberinto, root): #
        if laberinto['tipo'] == 'habitacion':
            obj=self.builder.fabricarHabitacion(laberinto['num'])
        elif laberinto['tipo'] == 'bomba':
            obj=self.builder.fabricarBombaHab(root)  
            
        hijos = laberinto.get('hijos', [])
        for hijo in hijos:
            self.crearLaberintoRecursivo(hijo, obj)
        
    def crearLaberinto(self):
        self.builder.fabricarLaberinto()
        for laberinto in self.director['laberinto']:
            self.crearLaberintoRecursivo(laberinto, 'root')
            
        for puerta in self.director['puertas']:
            self.builder.fabricarPuertaBuilder(puerta[0], puerta[1], puerta[2], puerta[3])
    
    def verConfig(self, ruta):
        self.director = json.load(open(ruta,'r'))
        
    def procesar(self, ruta):
        self.verConfig(ruta) #Cargo el JSON
        self.iniBuilder() #Inicializo el builder
        self.crearLaberinto() #Creo el laberinto
        self.crearJuego() #Creo el juego
