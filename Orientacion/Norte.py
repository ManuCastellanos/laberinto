from Orientacion import Orientacion

class Norte(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    def caminar(self, alguien):
        alguien.irAlNorte()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.norte(unEM)