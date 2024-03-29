from os import system
from time import sleep
from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf

#### ----- Sector de funciones -----

def crear_tablero(tamaño):
    tablero = []
    for i in range(tamaño):
        tablero.append(["#"]*tamaño)
    for i in range(tamaño):
        if i in range(1,10):
            tablero[i][0] =  " "+str(i)
        else:
            tablero[i][0] =  i
        for j in range(tamaño):
                tablero[0][j] =  j
    tablero [0][0]= "  "
    return tablero

def imprimir_tablero(tablero):
    largo = len(tablero)
    for i in range(largo):
        print ("")
        for j in range(largo):
            print (tablero [i][j], end="    ")
    print ("")

def armado_impresion_tablero(cant_jugadores):
    if cant_jugadores == 2:
        tamaño = 7
        tablero = crear_tablero(tamaño)
        imprimir_tablero(tablero)
        return tablero

    elif cant_jugadores == 3:
        tamaño = 10
        tablero = crear_tablero(tamaño)
        imprimir_tablero(tablero)
        return tablero

    elif cant_jugadores == 4:
        tamaño = 13 
        tablero = crear_tablero(tamaño)
        imprimir_tablero(tablero)
        return tablero

def nombre_jugadores(cant_jugadores):
    if cant_jugadores == 2:
        jug1 = input("\nIngrese el nombre del 1er jugador:\t")
        jug2 = input("\nIngrese el nombre del 2do jugador:\t")
        jug3 =""
        jug4 = ""
        
    elif cant_jugadores == 3:
        jug1 = input("\nIngrese el nombre del 1er jugador:\t")
        jug2 = input("\nIngrese el nombre del 2do jugador:\t")
        jug3 = input("\nIngrese el nombre del 3er jugador:\t")
        jug4 = ""

    elif cant_jugadores == 4:
        jug1 = input("\nIngrese el nombre del 1er jugador:\t")
        jug2 = input("\nIngrese el nombre del 2do jugador:\t")
        jug3 = input("\nIngrese el nombre del 3er jugador:\t")
        jug4 = input("\nIngrese el nombre del 4to jugador:\t")
    return (jug1,jug2,jug3,jug4)

# carga de fichas en el tablero
def cargar_ficha(jug, ficha, tablero):
    imprimir_tablero(tablero)
    sleep (3)
    print (f"\nEs el turno del jugador: {jug}.\n"
           "Debera ingresar la posicion de la fila, luego la de la columna.\n")
    sleep (3)
    cont = 0
    while cont != 1:
        try:
            pos_fila = int (input("Ingrese la fila donde quiere poner la ficha: \t"))
            pos_col = int (input("Ingrese la columna donde quiere poner la ficha: \t"))
        except ValueError:
            print ("Solo puede ingresar números.\n")
        pf = pos_fila 
        pc = pos_col 
        print (f"La posicion seleccionada es: {pos_fila}, {pos_col}\n")
        if tablero[pf][pc] == "#":
            tablero[pf][pc] = ficha
            cont += 1
            
        else:
            print ("\nLa posicion seleccionada ya esta ocupada por una ficha\n")
    
    return (tablero)

def control_ganador(tablero):
    fil = len(tablero)
    col = len(tablero[0])
    long = 4

    # Verificacion horizontal
    for i in range(fil):
        for j in range(col - long + 1):
            secuencia = tuple(tablero[i][k] for k in range(j, j + long))
            if len(set(secuencia)) == 1 and "#" not in secuencia:
                return True

    # Verificacion Vertical
    for i in range(fil - long + 1):
        for j in range(col):
            secuencia = tuple(tablero[k][j] for k in range(i, i + long))
            if len(set(secuencia)) == 1 and "#" not in secuencia:
                return True

    # Verificacion diagonal de izq a der
    for i in range(fil - long + 1):
        for j in range(col - long + 1):
            secuencia = tuple(tablero[i + k][j + k] for k in range(long))
            if len(set(secuencia)) == 1 and "#" not in secuencia:
                return True

    # Verificacion diagon der a izq
    for i in range(long - 1, fil):
        for j in range(col - long + 1):
            secuencia = tuple(tablero[i - k][j + k] for k in range(long))
            if len(set(secuencia)) == 1 and "#" not in secuencia:
                return True

    return False



    
#pasos para crear el juego: 1) determinar el nro de jugadores para determinar el tamñano del tablero.
#2) crear los jugadores.  3) crear el tablero  4) establecer las reglas  5) crear el codigo
#tablero para 2 jugadores 12x12  tablero para 3 personas 16x16  tableo para 4 personas 20x20
system("cls")
print ("\n\t\t\tBienvenido al juego 4 en linea\n")
print ("El objetivo del juego es formar con la figura del jugador 4 en linea.\n"
       "La inea puede ser horizintal, vertical o diagonal.\n"
       "La cantidad minima de jugadores es 2 y la cantidad maxima es 4.\n"
       "Cada jugador pondra una ficha por turno.\n"
    #    "El tiempo se determinara al iniciar la partida, y cada jugadr tendra 10 segundos para colocar su ficha"
    #    " luego de que halla acabado el tiempo del jugador anterior.\n"
       )
jug1 =""
ficha1 = "O"
jug2 =""
ficha2 = "X"
jug3 =""
ficha3 = "A"
jug4 =""
ficha4 = "H"
tablero =  []

while True:
    try:    
        cant_jugadores = int (input("Las opciones del juego son:\n"
                                    "1_ Para dos jugadores.\n"
                                    "2_ Para tres jugadores.\n"
                                    "3_ Para cuatro jugadores.\n"
                                    "4_ Para salir del juego.\n"
                                    "Ingrese una opcion:\n"))
        if cant_jugadores == 1:
            cant_jugadores = 2
            tablero = armado_impresion_tablero(cant_jugadores)
            jug1, jug2, jug3, jug4 = nombre_jugadores(cant_jugadores)
            contJugadas = 1
            ganador = False
            while ganador == False:
                if contJugadas == 1:
                    jug = jug1
                    ficha = ficha1
                elif contJugadas == 2:
                    jug = jug2
                    ficha = ficha2
                    contJugadas = 0
                try:
                    tablero1 = cargar_ficha (jug, ficha, tablero)
                except UnboundLocalError:
                    pass
                tablero = tablero1
                contJugadas += 1
                ganador = control_ganador (tablero)
                if ganador == True:
                    system ("cls")
                    print ("-------------------------\n|\t\t\t|\n|\tHAS GANADO\t|\n|\t\t\t|\n-------------------------")
                    sleep(3)

        elif cant_jugadores == 2:
            cant_jugadores = 3
            tablero = armado_impresion_tablero(cant_jugadores)
            jug1, jug2, jug3, jug4 = nombre_jugadores(cant_jugadores)
            contJugadas = 1
            ganador = False
            while ganador == False:
                if contJugadas == 1:
                    jug = jug1
                    ficha = ficha1
                elif contJugadas == 2:
                    jug = jug2
                    ficha = ficha2
                elif contJugadas == 3:
                    jug = jug3
                    ficha = ficha3
                    contJugadas = 0
                try:
                    tablero1 = cargar_ficha (jug, ficha, tablero)
                except UnboundLocalError:
                    pass
                tablero = tablero1
                contJugadas += 1
                ganador = control_ganador (tablero)
                if ganador == True:
                    system ("cls")
                    print ("-------------------------\n|\t\t\t|\n|\tHAS GANADO\t|\n|\t\t\t|\n-------------------------")
                    sleep(3)
            
        elif cant_jugadores == 3:
            cant_jugadores = 4
            tablero = armado_impresion_tablero(cant_jugadores)
            jug1, jug2, jug3, jug4 = nombre_jugadores(cant_jugadores)
            contJugadas = 1
            ganador = False
            while ganador == False:
                if contJugadas == 1:
                    jug = jug1
                    ficha = ficha1
                elif contJugadas == 2:
                    jug = jug2
                    ficha = ficha2
                elif contJugadas == 3:
                    jug = jug3
                    ficha = ficha3
                elif contJugadas == 4:
                    jug = jug4
                    ficha = ficha4
                    contJugadas = 0
                try:
                    tablero1 = cargar_ficha (jug, ficha, tablero)
                except UnboundLocalError:
                    pass
                tablero = tablero1
                contJugadas += 1
                ganador = control_ganador (tablero)
                if ganador == True:
                    system ("cls")
                    print ("-------------------------\n|\t\t\t|\n|\tHAS GANADO\t|\n|\t\t\t|\n-------------------------")
                    sleep(3)
            
        elif cant_jugadores == 4:
            salir_dyt_by_pf()
        else:   
            print ("Ingrese una opcion valida.")
    except ValueError:
        print ("Debe ingresar solo valores numéricos.")

        