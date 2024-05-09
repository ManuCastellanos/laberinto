from abc import ABC
from EM.ElementoMapa import ElementoMapa

class Item(ElementoMapa, ABC):
    def __init__(self):
        super().__init__()
    
    def usarItem(self, alguien):
        pass
    
    def esAgua(self):
        return False
    
    def esComida(self):
        return False
    