#TP Nro 4: Sentencias Repetitivas Determinadas
from random import randint
#1) Dada la siguiente lista de lenguajes, deberá obtener la siguiente salida
lenguajes = ["Python", "C", "Java", "Javascript", "Kotlin"]
# El 1° lenguaje que aprendi fue Python
# El 2° lenguaje que aprendi fue C
# El 3° lenguaje que aprendi fue Java
# El 4° lenguaje que aprendi fue Javascript
# El 5° lenguaje que aprendi fue Kothlin
for i in range (len(lenguajes)):
    print (f"El {i+1}° lenguaje que aprendi es: {lenguajes[i]}.")
print ("")

#2) Crear una lista que contenga las edades de sus compañeros y calcule la edad promedio del curso
edades = [21,18,23,33,42,20,18,23,22,29]
print (f"La lista de edades es: {edades}")
print (f"La edad promedio de las edades es: {sum(edades)/len(edades)}")
cont = 0
sum = 0
for i in edades:
    sum += edades[i]
    cont += 1
prom = sum / cont
print (f"La edad promedio de las edades es: {prom}")

# 3) Deberá crear una lista con los impuestos que pagó este último mes. Ahora imagine que usted cuenta 
# actualmente con $10000. ¿Cuántos impuestos alcanza a pagar y cuanto es la suma total que deberá pagar?
# Tenga en cuenta todas las posibilidades, si el monto le alcanza para pagar todo, algunos impuestos o solo uno, etc
sueldo = 10000
impuestos =  []
valorImpuestos = []
while True:
    tipoImp = input("Ingrese el tipo de impuesto: \n")

    if tipoImp == "":
        break
    else:
        valor = int (input("Ingrese el monto del impuesto: \n"))
        impuestos.append(tipoImp)
        valorImpuestos.append(valor)

for i in range(len(valorImpuestos)):
    print (f"El {i+1}° impuesto es: {impuestos[i]}; y su monto es de: ${valorImpuestos[i]}")

impPagado = []
impNoPagado = []
montoNoPagado = []
nuevoSaldo = 0
montoPagado = 0
for i in range(len(impuestos)):
    if valorImpuestos[i] <= sueldo:
        impPagado.append(impuestos[i])
        montoPagado += valorImpuestos[i]
        sueldo = sueldo - valorImpuestos[i]
        nuevoSaldo = sueldo
    elif valorImpuestos[i] > sueldo:
        impNoPagado.append(impuestos[i])
        montoNoPagado.append(valorImpuestos[i])

for i in impPagado:
    print (f"Impuesto pagado: {i}")

for i in range(len(impNoPagado)):
    print (f"Impuesto ´NO´ pagado: {impNoPagado[i]}, saldo: {montoNoPagado[i]}")
    
print (f"El total de impuestos pagados es: ${montoPagado}")
print (f"El saldo de su dinero es: ${nuevoSaldo}")

# 4) desarrolle un programa que pregunte al usuario si desea encontrar el numero mas grande o el
# mas chico de una serie de numeros ingresados por teclado.  y efectivamente el programa devolvera 
# el mas grande o el mas chico de todos los numeros ingresados

listaNumeros = []
while True:
    #num = int(input("Ingrese un numero distinto de 0.\nCuando ingrese 0 se terminara la ejecucion del programa de llenado.\n"))
    print ("Ingrese un numero distinto de 0.\nCuando ingrese 0 se terminara la ejecucion del programa de llenado.\n")
    num = randint(0,100) 
    if num != 0:
        listaNumeros.append(num)
    elif num == 0:
        break

print (listaNumeros)
listaNumeros.sort()
print (listaNumeros) 
print ("Si desea buscar el mayor de los numeros ingresados, presione M.\n"
       "Si desea buscar el menor de los numeros ingresados, presione m.\n")
opc = input("Ingrese una opcion:\n")
if opc == "M":
    print (f"El numero mas grande de la lista es: {listaNumeros[len(listaNumeros)-1]}")
elif opc == "m":
    print (f"El numero mas pequeño de la lista es: {listaNumeros[0]}")
else:
    print ("Opcion invalida.")

# 5) Desarrollar un programa que calcule cuantas formas existen para lograr un total de 10 entre 
# tres dados.  luego calcule la probabilidad de tirar un diez con precision a tres lugares.
conteo = 0
tiradas = 0
for dado1 in range(1, 7):
    for dado2 in range(1 , 7):
        for dado3 in range(1, 7):
            tiradas += 1
            #print (f"Tirada n° {tiradas}: dado1 = {dado1}, dado2 = {dado2}, dado3 = {dado3}")
            if dado1 + dado2 + dado3 == 10:
                conteo += 1
                print (f"Forma n° {conteo}: dado1 = {dado1}, dado2 = {dado2}, dado3 = {dado3}")
print (f"El total de tiradas que se pueden lograr es n° {tiradas}")  
print (f"El total de formas que se pueden lograr es n° {conteo}")
casosFavorables = conteo
numeroCasos = tiradas
prob10 = casosFavorables/numeroCasos
probCadaTres = round((3 * prob10 - 3 * (pow(prob10, 2)) + pow (prob10, 3))*100 , 2)
print (f"La probabilidad de tener un 10 cada 3 tiradas es de: {probCadaTres}%")

# desafio) Teniendo en cuenta los meses del año, en el primer mes el gasto en internet fue de 4000, pero el mismo 
#aumentó cada tres meses un 20%. ¿Cuánto pagó cada mes y cuanto pago en total en el abono de internet?
gastoInternet = 4000
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviemba", "Diciembre"]

gastoTotal = 0
cont = 0
for i in range(len(meses)):
    cont += 1
    if cont == 2:
        print (f"En el mes de {meses[i]}, el costo de internet fue de: ${gastoInternet}")
        gastoInternet = gastoInternet * 1.2
        gastoTotal = gastoTotal + gastoInternet
        cont = cont - 3
    elif cont < 2:
        gastoTotal = gastoTotal + gastoInternet
        print (f"En el mes de {meses[i]}, el costo de internet fue de: ${gastoInternet}")
print (f"El total abonado de internet fue de :{gastoTotal}")



