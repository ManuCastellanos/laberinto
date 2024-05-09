from EM.Container.Contenedor import Contenedor


class Cornucopia (Contenedor):
    def __init__(self, num):
        super().__init__(num)
        self.items = []
        
    def entrar(self,alguien):
        print(alguien, " está en la cornucopia", self.num)
        alguien.posicion = self
    
    def salir(self, alguien):
        print(alguien, " ha salido de la cornucopia", self.num)
        alguien.posicion = self.padre
    
    def obtenerComandos(self,alguien):
        lista = []
        if alguien.posicion == self:
            lista = super().obtenerComandos(None)
            for item in self.items:
                lista.append(item)
        else:
            lista= super().obtenerComandos(alguien)
    
    def cogerItem(self, alguien, item):
        alguien.inventario.agregarItem(item)
        self.items.remove(item)
        print("Se ha cogido ", item)
        
    def esCornucopia(self):
        return True
   
    def agregarItem(self, item):
        self.items.append(item)
        item.padre = self
        
    def __str__(self):
        salida="Cornucopia en " + str(self.num) + " con "
        
        for item in self.items:
            salida += "\n"+ item.__str__()
            
        return salida
         