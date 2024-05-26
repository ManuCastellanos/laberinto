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
        archivo= os.path.join(dir, 'laberinto/XML/labCompi.xml')
        director= Director()
        adapter= Adapter(archivo)
        director.procesar(adapter.get_json())
        self.juego= director.getJuego()
        prota = Personaje("Manolito")
        self.juego.iniProta(prota)

    def testLab(self):
        self.assertEqual(self.juego.laberinto is not None, True)
        self.assertEqual(len(self.juego.laberinto.hijos), 2)
        # Assert that the habitaciones have the correct types
        hab1 = self.juego.laberinto.hijos[0]
        hab2 = self.juego.laberinto.hijos[1]

        self.assertEqual(hab1.esHabitacion(), True)
        self.assertEqual(hab2.esHabitacion(), True)

        self.assertEqual(hab1.forma.norte.esPared(), True)
        self.assertEqual(hab1.forma.este.esPared(), True)
        self.assertEqual(hab1.forma.sur.esPuerta(), True)
        self.assertEqual(hab1.forma.oeste.esPared(), True)
        
        self.assertEqual(hab2.forma.norte.esPuerta(), True)
        self.assertEqual(hab2.forma.este.esPared(), True)
        self.assertEqual(hab2.forma.sur.esPared(), True)
        self.assertEqual(hab2.forma.oeste.esPared(), True)

    def testProta(self):
        self.assertEqual(self.juego.personaje is not None, True)
        self.assertEqual(self.juego.personaje.nombre, "Manolito")
    
    def testBichos(self):
        self.assertEqual(len(self.juego.bichos), 2)
        bicho1 = self.juego.bichos[0]
        bicho2 = self.juego.bichos[1]

        
        self.assertEqual(bicho1.posicion, self.juego.laberinto.hijos[0])
        self.assertEqual(bicho2.posicion,self.juego.laberinto.hijos[1])
        
        self.assertTrue(self.juego.bichos[0].modo, Agresivo)
        self.assertTrue(self.juego.bichos[1].modo, Perezoso)
        
    def testCompis(self):
        self.assertEqual(len(self.juego.compañeros), 2)
        compi1 = self.juego.compañeros[0]
        compi2 = self.juego.compañeros[1]
        
        self.assertTrue(self.juego.personaje.compi.modo, Blitz)
        
        self.assertEqual(compi1.posicion, self.juego.laberinto.hijos[0])
        self.assertEqual(compi2.posicion, self.juego.laberinto.hijos[1])
        
        self.assertTrue(self.juego.compañeros[0].modo, Blitz)
        self.assertTrue(self.juego.compañeros[1].modo, Aura)
       
if __name__ == '__main__':
    unittest.main()