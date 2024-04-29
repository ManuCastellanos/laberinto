import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Game.Juego import Juego 

class TestJuego(unittest.TestCase):
    def test_fabricarLaberinto2Habitaciones(self):
        juego = Juego()  # Assuming Juego is the class containing the fabricarLaberinto2Habitaciones method

        juego.fabricarLaberinto2Habitaciones()

        laberinto = juego.laberinto

        # Assert that the laberinto has two habitaciones
        self.assertEqual(len(laberinto.hijos), 2)

        # Assert that the habitaciones have the correct connections
        hab1 = laberinto.hijos[0]
        hab2 = laberinto.hijos[1]

        # Asserts de las paredes 
        self.assertEqual(hab1.norte.esPared(),True)
        self.assertEqual(hab1.este.esPared(), True)
        self.assertEqual(hab1.oeste.esPared(), True)
        
        self.assertEqual(hab2.norte.esPared(), False)
        self.assertEqual(hab2.sur.esPared(), True)
        self.assertEqual(hab2.este.esPared(), True)
        self.assertEqual(hab2.oeste.esPared(), True)
        
        # Asserts de las puertas
        self.assertEqual(hab1.norte.esPuerta(), False)
        self.assertEqual(hab1.sur.esPuerta(), True)
        self.assertEqual(hab1.este.esPuerta(), False)
        self.assertEqual(hab1.oeste.esPuerta(), False)
        
        self.assertEqual(hab2.norte.esPuerta(), True)
        self.assertEqual(hab2.sur.esPuerta(), False)
        self.assertEqual(hab2.este.esPuerta(), False)
        self.assertEqual(hab2.oeste.esPuerta(), False)
        
        # Assert that the puerta connects the habitaciones correctly
        puerta = hab1.sur
        self.assertEqual(puerta, hab2.norte)
        self.assertEqual(puerta.lado1, hab1)
        self.assertEqual(puerta.lado2, hab2)

if __name__ == '__main__':
    unittest.main()