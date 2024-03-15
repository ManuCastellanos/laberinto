from EM.ElementoMapa import ElementoMapa


class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Te has chocado con una pared")
        
    def entrar_alguien(self, alguien):
        print(f"{alguien} ha chocado con una pared")
    
    #Testing
    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"