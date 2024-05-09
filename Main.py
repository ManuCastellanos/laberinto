
from colorama import Fore, Style, init
from Adapter.Adapter import Adapter
from EM.Container.Laberinto import Laberinto
from Game.Juego import Juego
from LaberintoAFactory import LaberintoAFactory 
from Builder.Director import Director
from Orientation.Norte import Norte
from Orientation.Este import Este
from Orientation.Oeste import Oeste
from Orientation.Sur import Sur

while True:
    select = input(Fore.CYAN + "¿Donde quieres jugar?\n "+ Style.RESET_ALL + "1. Consola \n 2. Desde la Interfaz Gráfica \n 3. Salir\n")
    
    try:
        select = int(select)
        
        if select == 1:
            while True:
                init()
                lab = input(Fore.CYAN + "¿Qué tipo de laberinto deseas jugar?\n" + Style.RESET_ALL + Fore.LIGHTGREEN_EX + "1." + Style.RESET_ALL + "Builder\n" + Style.RESET_ALL + Fore.LIGHTGREEN_EX +  "2."+ Style.RESET_ALL + "Abstract Factory\n" + Style.RESET_ALL + Fore.LIGHTGREEN_EX +  "3." +Style.RESET_ALL+ "Salir\n")
                
                lab = int(lab)
                if lab == 1: 
                    select1 = input(Fore.LIGHTGREEN_EX + "¿A qué Laberinto quieres jugar?\n" + Style.RESET_ALL +
                                    "1. Lab. 2 Habitaciones con 2 bichos \n" +
                                    "2. Lab. 2 Habitaciones con 2 bichos y 2 bombas\n" +
                                    "3. Lab. 4 Habitaciones con 4 bichos y 2 bombas\n" +
                                    "4. Lab. 4 Habitaciones con 4 bichos, Tunel y Armario\n" +
                                    "5. Lab. Compi\n" + 
                                    "6. Lab. XML\n" + 
                                    "7. Lab. Hijos.xml\n" + Style.RESET_ALL)
                    
                    select1 = int(select1)
                    
                    switch = {
                    1: 'JSON/lab2hab2bichos.json',
                    2: 'JSON/lab2hab2bichos2bombas.json',
                    3: 'JSON/lab4hab4bichos2bom.json',
                    4: 'JSON/lab4habTunelArm.json',
                    5: 'JSON/labCompi.json',
                    6: 'XML/labCompi.xml',
                    7: 'XML/labHijos.xml'
                    }
                    archivo=switch.get(select1, "\n\nSelecciona una opción válida\n\n")
   
                    if archivo.endswith('.json'):
                        director= Director()
                        director.procesar(archivo)
                        juego= director.getJuego()
                        juego.iniProta("Imbécil")
                        juego.abrirPuertas()
                        juego.laberinto.hijos[0].forma.sur.entrar(juego.personaje)
                        juego.laberinto.hijos[1].forma.sur.entrar(juego.personaje)
                        juego.lanzoBichos()
                        juego.lanzoCompis()
                        
                        print(juego)
                        # juego.laberinto.hijos[2].forma.sur.entrar(juego.personaje)
                        # juego.laberinto.hijos[3].hijos[0].forma.oeste.entrar(juego.personaje)
                        
                        # print(juego.laberinto.hijos[3].hijos[0].items[0])
                        # print(juego.laberinto.hijos[3].hijos[0].items[1])
                        
                        # juego.laberinto.hijos[3].hijos[0].items[0].comandos[0].ejecutar(juego.personaje)
                        # juego.laberinto.hijos[3].hijos[0].items[0].comandos[0].ejecutar(juego.personaje)

                        # juego.personaje.inventario.verInventario()
                        
                        # juego.personaje.inventario.soltarItem(juego.personaje.inventario.items[0], juego.personaje)
                        
                    elif archivo.endswith('.xml'):
                        director= Director()
                        adapter= Adapter(archivo)
                        director.procesar(adapter.get_json())
                        juego= director.getJuego()
                        juego.iniProta("Imbécil")
                        print(adapter.get_json())
                        print(juego)
                    else:
                        print("Archivo no válido")
                        
                elif lab == 2:
                    juego= Juego()
                    af= LaberintoAFactory()
                    juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)
                    juego.iniProta("Imbécil")
                    print(juego)
                
                elif lab == 3:
                    break

        elif select == 2:
            print("Interfaz Gráfica por implementar")
        
        elif select == 3:
            break

            
    except ValueError:
            print(Fore.RED + "No es un número válido, intenta de nuevo\n")   
        