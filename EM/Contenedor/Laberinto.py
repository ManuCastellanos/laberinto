import EM.Contenedor.Contenedor as Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def agregarHabitacion(self, unaHabitacion):
        self.agregarHijo(unaHabitacion)
        self.habitaciones.append(unaHabitacion)

    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        hab = self.obtenerHabitacion(1)
        hab.entrar(alguien)

    def recorrer(self, unBloque):
        unBloque(self)

        for habitacion in self.habitaciones:
            habitacion.recorrer(unBloque)

    def numeroHabitaciones(self):
        return len(self.habitaciones)

    def obtenerHabitacion(self, unNum):
        return self.hijos[unNum - 1]
