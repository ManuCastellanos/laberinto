from Orientacion import Orientacion

class Oeste(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    def caminar(self, alguien):
        alguien.irAlOeste()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.oeste(unEM)