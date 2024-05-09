from Comandos.Coger import Coger

class Inventario():
    UnicaInstancia = None
    
    def __new__(cls):
        if not cls.UnicaInstancia:
            cls.UnicaInstancia = super().__new__(cls)
            cls.UnicaInstancia.items = []
            
        else:
            cls.UnicaInstancia.vaciarInventario()
        return cls.UnicaInstancia
    
    def vaciarInventario(self):
        self.items = {}
    
    def verInventario(self):
        print("Inventario: ")
        for item in self.items[:]: 
            print(item)
            
    def agregarItem(self, item):
        self.items.append(item)
        
        if any(comando.esCoger() for comando in item.comandos):
            self.quitarCoger(item)
        
        print("Se ha agregado ", item)
        
        
    def quitarCoger(self, item):
        for comando in item.comandos[:]:
            if comando.esCoger():
                item.quitarComando(comando)
        
                
    def quitarItem(self, item):
        self.items.remove(item)
        
        if any (comando.esSoltar() for comando in item.comandos):
            self.quitarSoltar(item)    
        
        print("Se ha quitado", item)
    
    
    def soltarItem(self, item, alguien):
        if item in self.items:
            self.quitarItem(item)
            for comando in item.comandos[:]:
                if comando.esSoltar() or comando.esUsar():
                    item.quitarComando(comando)
            
            item.agregarComando(Coger(), item)
            item.padre= alguien.posicion
            alguien.posicion.agregarItem(item)
            print("Se ha soltado ", item)
    
    
    