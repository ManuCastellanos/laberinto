
from colorama import Fore, Style, init
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
                                    "5. Lab. Compi \n" + Style.RESET_ALL)
                    
                    select1 = int(select1)
                    
                    switch = {
                    1: 'JSON/lab2hab2bichos.json',
                    2: 'JSON/lab2hab2bichos2bombas.json',
                    3: 'JSON/lab4hab4bichos2bom.json',
                    4: 'JSON/lab4habTunelArm.json',
                    5: 'JSON/labCompi.json'
                    }
                    archivo=switch.get(select1, "\n\nSelecciona una opción válida\n\n")
                    director= Director()

                    director.procesar(archivo)
                    juego= director.getJuego()
                    juego.iniProta("Imbécil")
                    juego.lanzoCompis()
                    print(juego)
                    
                    
                elif lab == 2:
                    juego= Juego()
                    af= LaberintoAFactory()
                    juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)
                    print(juego)
                
                elif lab == 3:
                    break

        elif select == 2:
            print("Interfaz Gráfica por implementar")
        
        elif select == 3:
            break

            
    except ValueError:
            print(Fore.RED + "No es un número válido, intenta de nuevo\n")   
        