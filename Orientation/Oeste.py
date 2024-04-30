from Orientation.Orientacion import Orientacion

class Oeste(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None

    
    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    
    def caminar(self, alguien):
        contenedor= alguien.posicion.forma
        contenedor.oeste.entrar(alguien)

    def ponerElementoEn(self, unEM, unContenedor):
        unContenedor.oeste=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.forma.oeste is not None:
            unContenedor.forma.oeste.recorrer(unBloque)
