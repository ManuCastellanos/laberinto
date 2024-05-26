

from Comandos.Comando import Comando


class Usar(Comando):
    
    def ejecutar(self, alguien):
        self.receptor.usarItem(alguien)
        if self.receptor.esComida():
            print("Yummy, yummy! Ahora tienes ", alguien.poder, " de poder!\n")
        else:
            print("¡Glup glyup! Ahora tienes ", alguien.vidas, " de vidas!\n")
        alguien.itemUsado= self.receptor
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Usar " + str(self.receptor)