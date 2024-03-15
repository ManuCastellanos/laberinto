from EM.Cont.Contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, unaHabitacion):
        self.agregarHijo(unaHabitacion)

    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        hab = self.obtenerHabitacion(1)
        hab.entrar(alguien)

    def recorrer(self, unBloque):
        print("Recorriendo laberinto:")
        for hijo in self.hijos:
            hijo.recorrer(unBloque)

    def numeroHabitaciones(self):
        return len(self.hijos)

    def obtenerHabitacion(self, unNum):
        return self.hijos[unNum - 1]

    def __str__(self):
        cad= f"\nLaberinto con {len(self.hijos)} habitaciones\n\n"
        for hab in self.hijos:
             cad += hab.__str__() + "\n"
        return cad
