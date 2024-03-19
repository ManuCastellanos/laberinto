from Mode.ModoBicho import ModoBicho

class Agresivo(ModoBicho):

    def actua(self, unBicho):
        super().actua(unBicho)
    
    def __str__(self):
        return 'Agresivo'

