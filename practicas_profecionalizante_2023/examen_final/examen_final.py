from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf
#       Funciones del programa
#   Funcion para indicar el maximo de numeros a ingresar
def num_maximo ():
    num_tot = 0
    while num_tot <= 0 :
        try:
            num_tot = int(input("Ingrese la totalidad de numeros para ingresar a la lista: \n"))
        except ValueError:
            print ("Debe ingresar solo números")
    return num_tot



#   Imprimir la lista
def imprimir_lista(lista_numeros): 
    largo = len(lista_numeros)
    for i in range(largo):
        print (f"El número {i+1}° es: {lista_numeros[i]}")

#   Localizar elmayor de los numeros
def localizar_mayor(lista_numeros):
    mayor = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > mayor:
            mayor = lista_numeros[i]
    return(mayor)

#   Localizar el menor de los numeros
def localizar_menor(lista_numeros):
    menor = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] < menor:
            menor = lista_numeros[i]
    return(menor)

def promedio(lista_numeros):
    suma = sum(lista_numeros)
    prom = suma/len(lista_numeros)
    return(prom)
def orden_ascendente(lista_numeros):
    lista = sorted(lista_numeros)
    print (f"Esta es la lista: {lista_numeros}\n"
           "Esta es la lista ordenada en forma ascendente:")
    for i in range(len(lista)):
        print (f"{i+1}) {lista[i]}")

def orden_descendente(lista_numeros):
    lista1 = sorted(lista_numeros)
    print (f"Esta es la lista: {lista_numeros}\n"
           "Esta es la lista ordenada en forma descendente:")
    lista = list(reversed(lista1))
    for i in range(len(lista)):
        print (f"{i+1}) {lista[i]}")

#   funcion para cargar numeros
def cargar_numero():
    try:
        num = int(input("Ingrese un número entero : \n"))
    except ValueError:
            print ("Debe ingresar solo números")
    try:
        return num
    except UnboundLocalError:
        print ("Error de variable indeterminada")


# creacion de la lista y carga de datos
lista_numeros = []

cont = 0
num_tot = num_maximo()
# Carga de datos sin funcion
# while cont < num_tot:
#     valor = False
#     try:
#         num = int(input("Ingrese un número entero : \n"))
#         valor = True
#     except ValueError:
#             print ("Debe ingresar solo números")
#     if valor == True:
#         lista_numeros.append(num)
#         cont +=1
while cont < num_tot:
    num = cargar_numero()
    if num == None:
        pass
    else:
        lista_numeros.append(num)
        cont +=1

# Menu del programa

while True:
    print("en el siguiente menu podra realizar diferentes funciones.  \n"
          "1_ para imprimir la lista.\n"
          "2_ para localizar el mayor número de la lista.\n"
          "3_ para localizar el menor número de la lista.\n"
          "4_ para mostrar el promedio de la lista.\n"
          "5_ Para ordenar en forma ascendente la lista.\n"
          "6_ Para ordenar en forma descendente la lista.\n"
          "7_ Para salir del sistema.\n")
    try:
        opc = int (input("Ingrese una opcion:\n"))
        if opc == 1:
            imprimir_lista(lista_numeros)
        elif opc == 2:
            mayor = localizar_mayor(lista_numeros)
            print (f"El mayor número de la lista es: {mayor}")
        elif opc == 3:
            menor = localizar_menor(lista_numeros)
            print (f"El menor número de la lista es: {menor}")
        elif opc == 4:
            prom = promedio(lista_numeros)
            print (f"El promedio de la lista es: {prom}")
        elif opc == 5:
            orden_ascendente(lista_numeros)
        elif opc == 6:
            orden_descendente(lista_numeros)
        elif opc == 7:
            salir_dyt_by_pf()
        else:
            print ("Ingrese una opcion permitida.\n")
    except ValueError:
        print ("Usted ingreso una letra.\nDebe ingresar solo números.")