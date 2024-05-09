from Comandos.Comando import Comando

class Soltar(Comando):
    
    def ejecutar(self, alguien):
        alguien.inventario.soltarItem(self.receptor, alguien)
    
    def esSoltar(self):
        return True
    
    def __str__(self):
        return "Soltar " + str(self.receptor)
    
    