from Orientation.Orientacion import Orientacion

class Norte(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def caminar(self, alguien):
        alguien.irAlNorte()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.norte=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.norte is not None:
            unContenedor.norte.recorrer(unBloque)
        