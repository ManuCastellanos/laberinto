import unittest
import sys
import os
import unittest
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
        archivo= os.path.join(dir, 'laberinto/JSON/2hab2bichos2bombas.json')
        director= Director()
        director.procesar(archivo)
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


    
    def testBomba(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in habitacion.hijos:
                if hijo.esBomba():
                    self.assertEqual(hijo is not None, True)
                    self.assertEqual(hijo.esBomba(), True)
    
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
        
       
if __name__ == '__main__':
    unittest.main()
