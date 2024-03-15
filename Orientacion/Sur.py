from Orientacion import Orientacion

class Sur(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    def caminar(self, alguien):
        alguien.irAlSur()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.sur(unEM)