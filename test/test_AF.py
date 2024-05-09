import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Game.Juego import Juego
from LaberintoAFactory import LaberintoAFactory 

class TestJuego(unittest.TestCase):
    def test_fabricarLaberinto4Hab4Bomb4BichosAF(self):
        juego = Juego()  

        af= LaberintoAFactory()

        juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)

        laberinto = juego.laberinto

        # Assert that the laberinto has four habitaciones
        self.assertEqual(len(laberinto.hijos), 4)

        # Assert that the habitaciones have the correct connections
        hab1 = laberinto.hijos[0]
        hab2 = laberinto.hijos[1]
        hab3= laberinto.hijos[2]
        hab4= laberinto.hijos[3]
        
        # Asserts de las paredes 
        self.assertEqual(hab1.forma.sur.esPuerta(),True)
        self.assertEqual(hab1.forma.este.esPuerta(), True)
        
        self.assertEqual(hab2.forma.este.esPuerta(), True)
        self.assertEqual(hab2.forma.norte.esPuerta(), True)
        
        self.assertEqual(hab3.forma.oeste.esPuerta(), True)
        self.assertEqual(hab3.forma.sur.esPuerta(), True)
        
        self.assertEqual(hab4.forma.norte.esPuerta(), True)
        self.assertEqual(hab4.forma.oeste.esPuerta(), True)
        
        # Asserts de las paredes
        self.assertTrue(hab1.forma.oeste.esPared())
        self.assertTrue(hab2.forma.oeste.esPared())
        self.assertTrue(hab3.forma.norte.esPared())
        self.assertTrue(hab4.forma.este.esPared())

        # Asserts de las bombas
        self.assertTrue(hab1.forma.norte.esParedBomba())
        self.assertTrue(hab2.forma.sur.esParedBomba())
        self.assertTrue(hab3.forma.este.esParedBomba())
        self.assertTrue(hab4.forma.sur.esParedBomba())

        # Asserts de los bichos
        self.assertEqual(len(juego.bichos), 4)
        bicho1 = juego.bichos[0]
        bicho2 = juego.bichos[1]
        bicho3 = juego.bichos[2]
        bicho4 = juego.bichos[3]
        
        self.assertEqual(bicho1.posicion, hab1)
        self.assertEqual(bicho2.posicion, hab3)
        self.assertEqual(bicho3.posicion, hab2)
        self.assertEqual(bicho4.posicion, hab4)
        
if __name__ == '__main__':
    unittest.main()