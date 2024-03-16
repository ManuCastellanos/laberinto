from EM.Pare.Pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Te has chocado con una pared-bomba")
        print("¡¡¡BOOOOOM!!!")

    def entrar_alguien(self, alguien):
        print(f"{alguien} ha chocado con una pared-bomba")
        print("¡¡¡BOOOOOM!!!")
    
    def recorrer(self, unBloque):
        pass
    
    def __str__ (self):
        return super().__str__() + " Bomba"
