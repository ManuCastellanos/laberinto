from EM.Hoj.Hoja import Hoja

class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em


    