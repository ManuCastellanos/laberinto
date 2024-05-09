from Comandos.Comando import Comando

class Coger(Comando):
    
    def ejecutar(self, alguien):
        alguien.inventario.agregarItem(self.receptor)
        
        for item in self.receptor.padre.items:
            if item == self.receptor:
                self.receptor.padre.items.remove(item)
                break
    
    def esCoger(self):
        return True

    def __str__(self):
        return "Coger " + self.receptor