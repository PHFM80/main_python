import datetime as dt

def hora():
    hoy = dt.datetime.today() 
    horaActual = hoy.strftime("%H:%M:%S")
    return horaActual
def fecha():
    hoy = dt.datetime.today()
    fechaActual = hoy.strftime("%d-%m-%y")
    return fechaActual

def imprimir_sala(filas, columnas):
    for i in range(filas):
        print ("")
        for j in range(columnas):
            print (sala[i][j], end="  ")

#ingresar datos de la butaca
def ingresar_butaca ():
    print ("Para seleccionar una butaca debera ingresar una letra de la A a la J, luego un número del 1 al 22.")
    fil = input("La letra de la fila:   ").upper()
    try:
        col = int(input("Ingrese el numero de la columna: "))
    except ValueError:
        print ("Debe ingresar solo numeros.")
    filT = False
    colT = False
    if fil not in filasLetras:
        print ("La letra ingresada no pertenece a esta sala.\nIngrese una letra adecuada.")
    else:
        filT = True
    if col < 1 or col > 22:
        print ("ingrese un numero adecuado a la sala")
    elif col == 11 or col == 12:
        print ("Ingreso la columna del pasillo")
    else:
        colT = True

    if colT == True and filT == True:
        print (f"La butaca seleccionada es: ({fil}, {col})")
        posicion = f"{fil}, {col}"
        return (posicion)

#verificar butaca desocupada
def butaca_desocupada ():
    pos = ingresar_butaca ()
    print (f"esta es la posicion retornada: {pos}")
    desocupada = False
    if pos != None:
        butacas =[]
        for i in range(filas):
            for j in range(columnas):
                butaSala = sala[i][j]
                butacas.append(butaSala)
        if pos in butacas:
            print ("Butaca desocupada")
            desocupada = True
        else:
            print ("Butaca ocupada")
    return (desocupada, pos)

# cargar datos si butaca esta desocupada
def cargar_datos():
    valido, pos = butaca_desocupada()
    datos = []
    if valido == True:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        nombreCompleto = nombre + ", " + apellido
        try:
            importe = int(input("Ingrese el importe abonado: "))
        except ValueError:
            print ("Debe ingresar solo numeros.")
        datos.append(pos)
        datos.append(f"     {nombreCompleto}")
        datos.append(importe)
        datos.append(fecha())
        datos.append(hora())
    return (datos, importe, pos)  

# realizar la impresion de los asientos
def listar_asientos(datos):
    for i in range(len(datos)):
        print("")
        for j in range(len(datos[i])):
            print (datos[i][j], end=("  "))



sala = []
datosGenerales = []
posOcupadas = []
filas = 10
filasLetras = "ABCDEFGHIJ"
columnas = 22
sumImporte = 0

    # Armado de la sala de cine, no es necesario modificarlo
# creacion de la matriz de la sala de cine
for i in range(filas):
    sala.append([" "]*columnas)
# Colocacion del pasillo en la sala de cine
for i in range(filas):
    for j in range(10, 12):
        sala[i][j] = "P"
# Cargado visual de los asientos
ii = 0
for i in (filasLetras):
    for j in range(columnas):
        if sala[ii][j] == "P":
            pass
        else:
            sala[ii][j] = f"{i}, {j+1}"
    ii += 1

datosGenerales.append(["UBICACION", "RESERVADO POR", "IMPORTE", "FECHA", "HORA"])
posOcupadas.append ("")

#Menu principal del programa
while True:
    try:
        print ("\n--- Menu principal del Cine ---\n")
        print ("1_ Reservar Asiento.\n"
            "2_ Eliminar Asiento Reservado.\n"
            "3_ Listar Asientos Reservedos.\n"
            "4_ Mostrar Butacas del cine.\n"
            "5_ Salir del programa.")
        opc = int (input ("Seleccione una opcion:\n"))

        if opc == 1:
            try:
                datos, importe, pos = cargar_datos()
                datosGenerales.append(datos)
                sumImporte += importe
                posOcupadas.append (pos)

                for i in range(filas):
                    for j in range(columnas):
                        butaSala = sala[i][j]
                        if butaSala == pos:
                            sala[i][j] = "ocup"
            except UnboundLocalError:
                pass

        elif opc == 2:
            fil = input("indique la fila: ").upper()
            for i in range(len (filasLetras)):
                if filasLetras[i] == fil:
                    print ("encontrado")
                    print (f"la poscicion es {i}")
                    filNum = i
            try:
                col = int (input("Indique la columna: "))
            except ValueError:
                pass
            buta = fil + ", " + str(col)
            col2 = col -1
            print (f"la butaca ingresada es: {buta}")
            print (f"esto es la lista posOcupadas {posOcupadas}")
            for i in range(len(posOcupadas)):
                print (i)
+
if posOcupadas[i] == buta:
                    datitos = datosGenerales [i]
                    for j in range(len(datitos)):
                        nuevoImporte = datitos[2]
                    sala [filNum][col2] = buta
                    posOcupadas.pop(i)
                    datosGenerales.pop(i)
                    sumImporte -= nuevoImporte

        elif opc == 3:
            listar_asientos (datosGenerales)
            print ("")
            print (f"\nEl total abonado de reservas es:\t\t${sumImporte}")

        elif opc == 4:
            imprimir_sala(filas, columnas)
            print ("")

        elif opc == 5:
            print ("Saliendo del programa.")
            break
        else:
            print ("Seleccione una opcion dentro del menu")
    except ValueError:
        print ("Ingreso una letra.\nDebe ingresar solo numeros.")
