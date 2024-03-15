from Modo import Modo

class Perezoso(Modo):

    def actua(self, unBicho):
        super().actua(unBicho)
    
    def __str__(self):
        return 'Perezoso'
    
    def __repr__(self, aStream):
        aStream.nextPutAll('Perezoso')
