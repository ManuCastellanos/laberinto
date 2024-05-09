

from Comandos.Comando import Comando


class Usar(Comando):
    
    def ejecutar(self, alguien):
        self.receptor.usarItem(alguien)
        
        alguien.itemUsado= self.receptor
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Usar " + str(self.receptor)