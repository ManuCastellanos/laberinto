from Orientacion import Orientacion

class Este(Orientacion):
    #Patrón: Singleton
    UnicaInstancia = None

    def caminar(self, alguien):
        alguien.irAlEste()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.este(unEM)