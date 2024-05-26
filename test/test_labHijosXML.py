import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Adapter.Adapter import Adapter
from Mode.CompañeroM.Aura import Aura
from Mode.CompañeroM.Blitz import Blitz

from Mode.BichosM.Agresivo import Agresivo
from Mode.BichosM.Perezoso import Perezoso
from Builder.Director import Director
from Game.Juego import Juego 
from Entes.Personaje import Personaje

class TestJuego(unittest.TestCase):
    def setUp(self):    
        super().setUp()
        self.juego = Juego()
        ruta= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        dir= os.path.dirname(ruta)
        archivo= os.path.join(dir, 'laberinto/XML/labHijos.xml')
        director= Director()
        adapter= Adapter(archivo)
        director.procesar(adapter.get_json())
        self.juego= director.getJuego()
        prota = Personaje("Manolito")
        self.juego.iniProta(prota)

    def testLab(self):
        self.assertEqual(self.juego.laberinto is not None, True)
        self.assertEqual(len(self.juego.laberinto.hijos), 4)
    # Assert that the habitaciones have the correct types
        hab1 = self.juego.laberinto.hijos[0]
        hab2 = self.juego.laberinto.hijos[1]
        hab3 = self.juego.laberinto.hijos[2]
        hab4 = self.juego.laberinto.hijos[3]

        self.assertEqual(hab1.esHabitacion(), True)
        self.assertEqual(hab2.esHabitacion(), True)
        self.assertEqual(hab3.esHabitacion(), True)
        self.assertEqual(hab4.esHabitacion(), True)

        self.assertEqual(hab1.forma.norte.esPared(), True)
        self.assertEqual(hab1.forma.este.esPared(), True)
        self.assertEqual(hab1.forma.sur.esPuerta(), True)
        self.assertEqual(hab1.forma.oeste.esPuerta(), True)
        
        self.assertEqual(hab2.forma.norte.esPared(), True)
        self.assertEqual(hab2.forma.este.esPuerta(), True)
        self.assertEqual(hab2.forma.sur.esPuerta(), True)
        self.assertEqual(hab2.forma.oeste.esPared(), True)
        
        self.assertEqual(hab3.forma.norte.esPuerta(), True)
        self.assertEqual(hab3.forma.este.esPuerta(), True)
        self.assertEqual(hab3.forma.sur.esPared(), True)
        self.assertEqual(hab3.forma.oeste.esPared(), True)
        
        self.assertEqual(hab4.forma.norte.esPuerta(), True)
        self.assertEqual(hab4.forma.este.esPared(), True)
        self.assertEqual(hab4.forma.sur.esPared(), True)
        self.assertEqual(hab4.forma.oeste.esPuerta(), True)
        
    # Assert that the habitaciones have the correct hijos
        self.assertEqual(len(hab1.hijos), 1)
        self.assertEqual(len(hab2.hijos), 1)
        self.assertEqual(len(hab3.hijos), 1)
        self.assertEqual(len(hab4.hijos), 1)

        self.assertEqual(hab1.hijos[0].esTunel(), True)
        self.assertEqual(hab2.hijos[0].esBomba(), True)
        self.assertEqual(hab3.hijos[0].esArmario(), True)
        self.assertEqual(hab4.hijos[0].esCornucopia(), True)
    
    def testTunel(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in habitacion.hijos:
                if hijo.esTunel():
                    self.assertEqual(hijo is not None, True)
                    self.assertEqual(hijo.esTunel(), True)    
    
    def testArmario(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in habitacion.hijos:
                if hijo.esArmario():
                    self.assertEqual(hijo is not None, True)
                    self.assertEqual(hijo.esArmario(), True)
    
    def testBomba(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in habitacion.hijos:
                if hijo.esBomba():
                    self.assertEqual(hijo is not None, True)
                    self.assertEqual(hijo.esBomba(), True)
    
    def testCornucopia(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in habitacion.hijos:
                if hijo.esCornucopia():
                    self.assertEqual(hijo is not None, True)
                    self.assertEqual(hijo.esCornucopia(), True)
                    
                    for item in hijo.hijos:
                        self.assertEqual(item.esItem(), True)
                        
    def testProta(self):
        self.assertEqual(self.juego.personaje is not None, True)
        self.assertEqual(self.juego.personaje.nombre, "Manolito")
    
    def testBichos(self):
        self.assertEqual(len(self.juego.bichos), 4)
        bicho1 = self.juego.bichos[0]
        bicho2 = self.juego.bichos[1]
        bicho3 = self.juego.bichos[2]
        bicho4 = self.juego.bichos[3]
        
        self.assertEqual(bicho1.posicion, self.juego.laberinto.hijos[0])
        self.assertEqual(bicho2.posicion,self.juego.laberinto.hijos[1])
        self.assertEqual(bicho3.posicion, self.juego.laberinto.hijos[2])
        self.assertEqual(bicho4.posicion, self.juego.laberinto.hijos[3])
        
        self.assertTrue(self.juego.bichos[0].modo, Agresivo)
        self.assertTrue(self.juego.bichos[1].modo, Perezoso)
        self.assertTrue(self.juego.bichos[2].modo, Agresivo)
        self.assertTrue(self.juego.bichos[3].modo, Perezoso)
        
    def testCompis(self):
        self.assertEqual(len(self.juego.compañeros), 2)
        compi1 = self.juego.compañeros[0]
        compi2 = self.juego.compañeros[1]
        
        self.assertEqual(compi1.posicion, self.juego.laberinto.hijos[2])
        self.assertEqual(compi2.posicion, self.juego.laberinto.hijos[3])
        
        self.assertTrue(self.juego.compañeros[0].modo, Aura)
        self.assertTrue(self.juego.compañeros[1].modo, Blitz)
       
if __name__ == '__main__':
    unittest.main()