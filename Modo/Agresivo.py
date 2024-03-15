from Modo import Modo

class Agresivo(Modo):

    def actua(self, unBicho):
        super().actua(unBicho)
    
    def __str__(self):
        return 'Agresivo'

    def __repr__(self, aStream):
        aStream.nextPutAll('Agresivo')
