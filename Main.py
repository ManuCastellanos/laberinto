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
                abierta1= False
                abierta2= False
                abierta3= False
                abierta4= False
                
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
                                                  "6." +Fore.LIGHTWHITE_EX+"Abrir Puerta "+Fore.LIGHTGREEN_EX+ str(juego.laberinto.hijos[0].obtenerComandos(juego.personaje)) + "\n" +
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
                                    abierta1= False
                                    abierta2= False
                                    abierta3= False
                                    abierta4= False
                                    abierta= False
                                else:
                                    juego.abrirPuertas()
                                    abierta1= True
                                    abierta2= True
                                    abierta3= True
                                    abierta4= True
                                    abierta= True
                                    
                            elif (num== 3):
                                while True:
                                    if len(juego.bichos) == 0:
                                        print("No hay bichos")
                                        if len(juego.compañeros) > 0:
                                            juego.lanzoCompis()
                                        break
                                    elif len(juego.compañeros) == 0:
                                        print("No hay compañeros")
                                        if len(juego.bichos) > 0:
                                            juego.lanzoBichos()
                                        break
                                    else:
                                        juego.lanzoBichos()
                                        juego.lanzoCompis()
                                        print("HILOS DE BICHOS Y COMPIS OPERATIVOS")
                                        break
                            
                            elif (num==4):
                                juego.finJuego()
                                print("Se acabó la fiesta de los hilos")
                                
                            elif(num==5):
                                hayTunel = False
                                for tunel in juego.personaje.posicion.hijos:
                                    if tunel.esTunel():
                                        hayTunel = True
                                        tunel.entrar(juego.personaje)
                                        print("Entrando en tunel")
                                        break
                                    if hayTunel:
                                        break
                            
                            elif(num==6):
                                if abierta1 == False or abierta2 == False or abierta3 == False or abierta4 == False:
                                    print("¿Qué puerta vas a abrir",juego.personaje.nombre,'?')
                                    print("Estan en la habitación: \n",juego.personaje.posicion)
    
                                    puerta = input("1. Puerta Norte\n2. Puerta Sur\n3. Puerta Este\n4. Puerta Oeste\n")
                                    puerta = int(puerta)
                                    if puerta == 1 and abierta1 == False:
                                        if juego.personaje.posicion.forma.norte.esPuerta():
                                            juego.personaje.posicion.forma.norte.comandos[0].ejecutar(juego.personaje)
                                            abierta1= True
                                        else:
                                            print("No hay puerta en esa dirección")
                                    elif puerta == 2 and abierta2 == False:
                                        if juego.personaje.posicion.forma.sur.esPuerta():
                                            juego.personaje.posicion.forma.sur.comandos[0].ejecutar(juego.personaje)
                                            abierta2= True
                                        else:
                                            print("No hay puerta en esa dirección")

                                    elif puerta == 3 and abierta3 == False:
                                        if juego.personaje.posicion.forma.este.esPuerta():
                                            juego.personaje.posicion.forma.este.comandos[0].ejecutar(juego.personaje)
                                            abierta3= True
                                        else:
                                            print("No hay puerta en esa dirección")                        
                                    elif puerta == 4 and abierta4 == False:
                                        if juego.personaje.posicion.forma.oeste.esPuerta():
                                            juego.personaje.posicion.forma.oeste.comandos[0].ejecutar(juego.personaje)
                                            abierta4= True
                                        else:
                                            print("No hay puerta en esa dirección")
                                    else:
                                        print("\n\nOpción no válida.\n\n")
                                else:
                                    print("Están todas las puertas cerradas")
                                    
                            elif(num==7):
                                if abierta1 == True or abierta2 == True or abierta3 == True or abierta4 == True:
                                
                                    print("¿Qué puerta vas a cerrar",juego.personaje.nombre,'?')
                                    print("Estan en la habitación: \n",juego.personaje.posicion)
 
                                    puerta = input("1. Puerta Norte\n2. Puerta Sur\n3. Puerta Este\n4. Puerta Oeste\n")
                                    puerta = int(puerta)
                                    if puerta == 1 and abierta1 == True:
                                        if juego.personaje.posicion.forma.norte.esPuerta():
                                            juego.personaje.posicion.forma.norte.comandos[0].ejecutar(juego.personaje)
                                            abierta= False
                                        else:
                                            print("No hay puerta en esa dirección")
                                    elif puerta == 2 and abierta2 == True:
                                        if juego.personaje.posicion.forma.sur.esPuerta():
                                            juego.personaje.posicion.forma.sur.comandos[0].ejecutar(juego.personaje)
                                            abierta= False
                                        else:
                                            print("No hay puerta en esa dirección")
                                
                                    elif puerta == 3 and abierta3 == True:
                                        if juego.personaje.posicion.forma.este.esPuerta():
                                            juego.personaje.posicion.forma.este.comandos[0].ejecutar(juego.personaje)
                                            abierta= False
                                        else:
                                            print("No hay puerta en esa dirección")                        
                                    elif puerta == 4 and abierta4 == True:
                                        if juego.personaje.posicion.forma.oeste.esPuerta():
                                            juego.personaje.posicion.forma.oeste.comandos[0].ejecutar(juego.personaje)
                                            abierta= False
                                        else:
                                            print("No hay puerta en esa dirección")
                                    else:
                                        print("\n\nOpción no válida.\n\n")        
                                else:
                                    print("Están todas las puertas abiertas")
                                    
                            elif (num==8):
                                print("¿A donde quieres ir ",juego.personaje.nombre,'?')
                                print("Estás en la habitación: ",juego.personaje.posicion)
                                
                                direccion = input("N. Norte\nS. Sur\nE. Este\nO. Oeste\n")
                                if direccion == 'N' or direccion == 'n':
                                    juego.personaje.irAlNorte()
                                elif direccion == 'S' or direccion == 's':
                                    juego.personaje.irAlSur()
                                elif direccion == 'E' or direccion == 'e':
                                    juego.personaje.irAlEste()
                                elif direccion == 'O' or direccion == 'o':
                                     juego.personaje.irAlOeste()
                                else:
                                    print(Fore.RED +"\n\nOpción no válida.\n\n")
                            elif (num==9):
                                hayCornucopia = False
                                
                                for hijo in juego.personaje.posicion.hijos:
                                    
                                    if hijo.esCornucopia():
                                        hayCornucopia = True
                                        hijo.entrar(juego.personaje)
                                        print("Entrando en cornucopia")
                                        while juego.personaje.posicion == hijo:
                                                coger = []
                                                print("¿Qué quieres hacer en la cornucopia ",juego.personaje.nombre,'?')
                                                
                                                accion = input("1. Coger\n2. Salir\n")
                                                accion = int(accion)
                                                
                                                if accion == 1:
                                                    contPara = 0
                                                    print("Hay "+ str(len(hijo.items)) +" paracaidas en la cornucopia:")
                                                    
                                                    for paracaidas in hijo.items:
                                                        
                                                        contPara += 1
                                                        print(str(contPara)+". "+str(paracaidas)+" (Puedes cogerlo)")
                                                        coger.append(True)
                                                        
                                                    obj= input("¿Qué paracaidas quieres coger? (Introduce el número)\n")
                                                    obj= int(obj)
                                                    print("Has seleccionado: ", obj, "coger:", str(coger))
                                                    if coger[obj-1] <= len(coger):
                                                        
                                                        if obj>=0 and obj<=len(coger):
                                                            hijo.cogerItem(juego.personaje, hijo.items[obj-1])

                                                    if len(hijo.items) == 0:
                                                        print("No hay más paracaidas en la cornucopia")
                                                        break
                                                    
                                                    else:
                                                        print("Puedes seguir cogiendo paracaidas")
                                                        
                                                elif accion == 2:
                                                    hijo.salir(juego.personaje)
                                                    print("Saliendo de la cornucopia")
                                                    break
                                                
                                if hayCornucopia is False:
                                    print("No hay cornucopia en la habitación")
                                    break
                            
                            elif (num==10):
                                if juego.personaje.compi is not None:
                                    print(juego.personaje.compi.__str__()+" es tu amigui")
                                else:
                                    print("No tienes compañero")
                            
                            elif (num==11):
                                itemSelect=None
                                
                                print("Tienes los siguientes paracaidas: \n")
                                for i, item in enumerate(juego.personaje.inventario.items):
                                    print(str(i+1)+". "+str(item))
                                
                                comand= input("¿Quieres seleccionar algún paracaidas?\n")
                                comand= int(comand)
                                itemSelect= juego.personaje.inventario.items[comand-1]
                                print("Has seleccionado: ", itemSelect)
                                
                                print(itemSelect.obtenerComandos(juego.personaje))
                                
                                comandos = itemSelect.obtenerComandos(juego.personaje)
                                for i, comand in enumerate(comandos):
                                    print(str(i+1)+". "+str(comand))
                                
                                accion= input("¿Qué quieres hacer con el paracaidas?\n")
                                accion= int(accion)
                                
                                if accion>0 and accion<=len(comandos):
                                    comandos[accion-1].ejecutar(juego.personaje)
                            
                            elif (num==12):
                                print(juego)
                            
                            elif (num==13):
                                break
                            
                        except ValueError:
                            print(Fore.RED + "No es un número válido, intenta de nuevo\n"+Style.RESET_ALL)    
        
        elif select == 2:
            print("Interfaz Gráfica por implementar")
        
        elif select == 3:
            break

            
    except ValueError:
            print(Fore.RED + "No es un número válido, intenta de nuevo\n")   
        