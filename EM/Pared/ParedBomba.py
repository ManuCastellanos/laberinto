import Pared

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
    
    
