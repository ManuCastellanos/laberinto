
from Comandos.Coger import Coger
from Items.Item import Item
import random


class Comida(Item):
    
    def __init__(self):
        super().__init__()
        self.valor = random.randint(1, 5)
        self.agregarComando(Coger(), self)
        
    def esComida(self):
        return True
    
    def usarItem(self, alguien):
        alguien.poder += self.valor
        alguien.inventario.quitarItem(self)
        
        for comando in self.comandos:
            if comando.esUsar():
                self.quitarUsar(comando)
    
    def quitarUsar(self, comando):
        self.quitarComando(comando)
    
    def __str__(self):
        return "Comida con valor de " + str(self.valor)
                     