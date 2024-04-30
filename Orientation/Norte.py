from Orientation.Orientacion import Orientacion

class Norte(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def caminar(self, alguien):
        contenedor= alguien.posicion.forma
        contenedor.norte.entrar(alguien)

    def ponerElementoEn(self, unEM, unContenedor):
        unContenedor.norte=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.forma.norte is not None:
            unContenedor.forma.norte.recorrer(unBloque)
        