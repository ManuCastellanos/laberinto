from Orientation.Orientacion import Orientacion

class Oeste(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    
    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    
    def caminar(self, alguien):
        alguien.irAlOeste()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.oeste=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.oeste is not None:
            unContenedor.oeste.recorrer(unBloque)
