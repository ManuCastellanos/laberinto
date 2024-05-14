from colorama import Fore, Style, init
from Adapter.Adapter import Adapter
from EM.Container.Laberinto import Laberinto
from Entes.Personaje import Personaje
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
                                    "1. 2 Habitaciones con 2 bichos \n" +
                                    "2. 2 Habitaciones con 2 bichos y 2 bombas\n" +
                                    "3. 4 Habitaciones con 4 bichos y 2 cornucopias\n" +
                                    "4. 2 Habitaciones con 2 bichos y 2 compis\n" +
                                    "5. Laberinto completo\n" + 
                                    "6. Lab. XML\n" + 
                                    "7. Lab. Hijos.xml\n" + Style.RESET_ALL)
                    
                    select1 = int(select1)
                    
                    switch = { 
                    1: 'JSON/2hab2bichos.json',
                    2: 'JSON/2hab2bichos2bombas.json',
                    3: 'JSON/4hab4bichos2bom.json',
                    4: 'JSON/labCompi.json',
                    5: 'JSON/labcompleto.json',
                    6: 'XML/labCompi.xml',
                    7: 'XML/labHijos.xml'
                    }
                    archivo=switch.get(select1, "\n\nSelecciona una opción válida\n\n")
   
                    if archivo.endswith('.json'):
                        director= Director()
                        director.procesar(archivo)
                        juego= director.getJuego()
                        #juego.laberinto.hijos[0].forma.sur.entrar(juego.personaje)
                        #juego.laberinto.hijos[1].forma.sur.entrar(juego.personaje)
                        
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
                        
                    else:
                        print("Archivo no válido")
                        
                elif lab == 2:
                    juego= Juego()
                    af= LaberintoAFactory()
                    juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)
                
                elif lab == 3:
                    break
                
                activada= False
                abierta= False
                
                #Mi juego siempre va a tener un personaje
                prota = Personaje(input("Introduce el nombre del personaje: ")) 
                juego.iniProta(prota)
                print(juego)
                
                while juego.fase.esFinal() == False:
            
                        num = input(Fore.MAGENTA+"\n¿Qué quieres hacer?\n"+Fore.LIGHTGREEN_EX+
                                                  "0."+Fore.LIGHTWHITE_EX+ "Atacar\n"+Fore.LIGHTGREEN_EX+
                                                  "1." +Fore.LIGHTWHITE_EX+"Activar/Desactivar las Bombas\n" +Fore.LIGHTGREEN_EX +
                                                  "2." +Fore.LIGHTWHITE_EX+"Abrir/Cerrar las Puertas\n"+Fore.LIGHTGREEN_EX+
                                                  "3." +Fore.LIGHTWHITE_EX+"Lanzar Hilos\n" + Fore.LIGHTGREEN_EX+
                                                  "4." +Fore.LIGHTWHITE_EX+"Terminar Hilos\n"+Fore.LIGHTGREEN_EX+
                                                  "5." +Fore.LIGHTWHITE_EX+"Entrar en tunel\n"+Fore.LIGHTGREEN_EX+
                                                  "6." +Fore.LIGHTWHITE_EX+"Abrir Puerta "+Fore.LIGHTGREEN_EX+ 
                                                  "7." +Fore.LIGHTWHITE_EX+"Cerrar Puerta\n"+Fore.LIGHTGREEN_EX+
                                                  "8." +Fore.LIGHTWHITE_EX+"Mover personaje\n"+Fore.LIGHTGREEN_EX+
                                                  "9." +Fore.LIGHTWHITE_EX+"Entrar a la cornucopia\n"+Fore.LIGHTGREEN_EX+
                                                  "10." +Fore.LIGHTWHITE_EX+"¿Quién es mi compañero?\n"+ Fore.LIGHTGREEN_EX+
                                                  "11." +Fore.LIGHTWHITE_EX+"¿Qué tengo en el inventario?\n"+Fore.LIGHTGREEN_EX+ 
                                                  "12." +Fore.LIGHTWHITE_EX+"Imprimir laberinto\n"+ Fore.LIGHTGREEN_EX+
                                                  "13." +Fore.LIGHTWHITE_EX+"Salir\n"+Style.RESET_ALL)
                        
                        try:
                            num= int(num)
                            if (num== 0):
                                    juego.personaje.atacar()

                            elif (num== 1):
                                if activada:
                                    juego.desactivarBombas()
                                    activada= False
                                else:
                                    juego.activarBombas()
                                    activada= True

                            elif (num== 2):
                                if abierta:
                                    juego.cerrarPuertas()
                                    abierta= False
                                else:
                                    juego.abrirPuertas()
                                    abierta= True

                            elif (num== 3):
                                pass
                            elif (num==4):
                                pass
                            elif (num==8):
                                print("¿A donde quieres mover a ",juego.personaje.nombre,'?')
                                print("El personaje esta en la habitacion: ",juego.personaje.posicion)
                                
                                direccion = input("W. Norte\nS. Sur\nD. Este\nA. Oeste\n")
                                if direccion == 'W' or direccion == 'w':
                                    juego.personaje.irAlNorte()
                                elif direccion == 'S' or direccion == 's':
                                    juego.personaje.irAlSur()
                                elif direccion == 'D' or direccion == 'd':
                                    juego.personaje.irAlEste()
                                elif direccion == 'A' or direccion == 'a':
                                     juego.personaje.irAlOeste()
                                else:
                                    print("\n\nOpción no válida.\n\n")
                        except ValueError:
                            print(Fore.RED + "No es un número válido, intenta de nuevo\n")    
        
        elif select == 2:
            print("Interfaz Gráfica por implementar")
        
        elif select == 3:
            break

            
    except ValueError:
            print(Fore.RED + "No es un número válido, intenta de nuevo\n")   
        