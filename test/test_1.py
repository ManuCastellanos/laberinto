import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Builder.Director import Director
from Game.Juego import Juego 
from Mode.BichosM.Agresivo import Agresivo
from Mode.BichosM.Perezoso import Perezoso

class TestJuego(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.juego = Juego()
        ruta= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        dir= os.path.dirname(ruta)
        archivo= os.path.join(dir, 'laberinto/JSON/2hab2bichos.json')
        director= Director()
        director.procesar(archivo)
        self.juego= director.getJuego()
        self.juego.iniProta("Imbécil")
        
    def testLab(self):
        self.assertEqual(self.juego.laberinto is not None, True)
        self.assertEqual(len(self.juego.laberinto.hijos), 2)
    
    def testBichos(self):
        self.assertEqual(len(self.juego.bichos), 2)
        
        self.assertEqual(self.juego.bichos[0].posicion is not None, True)
        self.assertEqual(self.juego.bichos[1].posicion is not None, True)
        
        self.assertTrue(self.juego.bichos[0].modo, Agresivo)
        self.assertTrue(self.juego.bichos[1].modo, Perezoso)
        
        
if __name__ == '__main__':
    unittest.main()