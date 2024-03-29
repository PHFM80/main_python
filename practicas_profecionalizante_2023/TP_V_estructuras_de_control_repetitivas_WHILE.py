#1) Dada la siguiente lista de lenguajes, deberá obtener la siguiente salida
lenguajes = ["Python", "C", "Java", "Javascript", "Kotlin"]
# El 1° lenguaje que aprendi fue Python
# El 2° lenguaje que aprendi fue C
# El 3° lenguaje que aprendi fue Java
# El 4° lenguaje que aprendi fue Javascript
# El 5° lenguaje que aprendi fue Kothlin

contIndice = 0
while contIndice < len(lenguajes):
    elemento = lenguajes[contIndice]
    print (f"El {contIndice+1}° lenguaje que aprendi fue {elemento}")
    contIndice += 1

#2) Crear una lista que contenga las edades de sus compañeros y calcule la edad promedio del curso
edades = [21,18,23,33,42,20,18,23,22,29]
cont = 0
sumEdades = 0
while cont < len(edades):
    edad = edades[cont]
    sumEdades += edad
    cont += 1
print (f"El promedio de las edades es: {sumEdades/cont}")


# 3) Deberá crear una lista con los impuestos que pagó este último mes. Ahora imagine que usted cuenta 
# actualmente con $10000. ¿Cuántos impuestos alcanza a pagar y cuanto es la suma total que deberá pagar?
# Tenga en cuenta todas las posibilidades, si el monto le alcanza para pagar todo, algunos impuestos o solo uno, etc
sueldo = 10000
impuestos =  []
valorImpuestos = []
contImpuesto = 0
cantImpuestos = int (input("ingrese cuantos impuestos va a cargar: "))
while contImpuesto < cantImpuestos:
    impuesto = input("Ingrese el tipo de impuesto: \n")
    monto = int (input("Ingrese el monto del impuesto: \n"))
    impuestos.append(impuesto)
    valorImpuestos.append(monto)
    contImpuesto += 1
impPagados = 0
impImpagos = 0
cont = 0
totPagados = 0
totImpagos = 0
print (impuestos)
print (valorImpuestos)
while cont < len(impuestos):
    if valorImpuestos[cont] < sueldo:
        sueldo -= valorImpuestos[cont]
        impPagados += 1
        totPagados += valorImpuestos[cont]
        print (f"Usted pago el impuesto de: {impuestos[cont]}, por un valor de: ${valorImpuestos[cont]}")
    else:
        impImpagos += 1
        totImpagos += valorImpuestos[cont]
        print (f"Usted no pago el impuesto de: {impuestos[cont]}, por un valor de: ${valorImpuestos[cont]}")
    cont += 1
print (f"Usted pago {impPagados} impuestos, por un valor de: ${totPagados}")
print (f"Usted no pago {impImpagos} impuestos, por un valor de: ${totImpagos}")


# 4) desarrolle un programa que pregunte al usuario si desea encontrar el numero mas grande o el
# mas chico de una serie de numeros ingresados por teclado.  y efectivamente el programa devolvera 
# el mas grande o el mas chico de todos los numeros ingresados

from random import randint as rd
listaNumeros = []
cantNum = int (input("Ingrese la cantidad de numeros que desea generar: "))
rangoMenor = int (input("Ingrese desde donde quiere generar numeros. "))
rm = rangoMenor
rangoMayor = int (input("Ingrese hasta donde quiere generar numeros. "))
RM = rangoMayor
cont = 0
while cont < cantNum:
    listaNumeros.append(rd(rm, RM))
    cont += 1
numMenor = RM
numMayor = rm
cont1 = 0
while cont1 < len(listaNumeros):
    elemento = listaNumeros[cont1]
    if elemento < numMenor:
        numMenor = elemento
    elif elemento > numMayor:
        numMayor = elemento
    cont1 += 1
print (f"El mayor de los numeros de la lista es: {numMayor}")
print (f"El menor de los numeros de la lista es: {numMenor}")
print (listaNumeros)

# 5) ingrese una frase por teclado.  Luego calcule la cantidad de vocales, consonantes y otros
# caracteres que se encuentran en dicha frase.  imprima estos calculos.
vocales = "aeiou"
consonantes = "qwrtypsdghjklñzxcvbnm"

frase = input("Ingrese una frase para analizar: \n").lower()
cont = 0 
contV = 0
contC = 0
contO = 0
contVacio = 0
while cont < len(frase):
    elemento = frase[cont]
    if elemento in vocales:
        contV += 1
    elif elemento in consonantes:
        contC += 1
    elif elemento == " ":
        contVacio += 1
    else:
        contO += 1
    cont += 1
print (f"La cantidad de vocales es: {contV}\n"
       f"La cantidad de consonantes es: {contC}\n"
       f"La cantidad de espacios vacios es: {contVacio}\n"
        f"La cantidad de otros elementos es: {contO}\n")

# 6) Desafio.  Desarrolle un programa que analice una frase.  el programa determinara:
# 1_ cantidad de caracteres de la frase
# 2_ cantidad de consonantes
# 3_ cantidad de de caracteres especiales
# 4_ cantidad y posicion de mayusculas
# 5_ cantidad y posicion de vocales
# 6_ validar la entrada para no colocar entradas no validas

vocMin = "aeiou"
vocMay = "AEIOU"
vocales = vocMay + vocMin
consMin = "qwrtypsdfghjklñzxcvbnm"
consMay = "QWRTYPSDFGHJKLÑZXCVBNM"
consonates = consMay + consMin
caracteres = vocMay+vocMin+consMay+consMin
mayusculas = vocMay+consMay
#frase = input("Ingrese una frase: \n")
frase = "Mala !$& es Al ... Ejemplo"

cont = 0 
contVacio = 0
contConsonantes = 0
contEspeciales = 0
contMayusculas = 0
contVocales = 0
posMayusculas = []
posVocales = []
print (frase)
while cont < len(frase):
    elemento = frase[cont]
    print (f"la posicion es {cont+1} y el elemnto es {elemento}")
    if elemento == " ":
        contVacio += 1
    elif elemento in consonates:
        contConsonantes += 1
    elif elemento not in caracteres:
        contEspeciales += 1
    elif elemento in mayusculas: 
        posMayusculas.append(cont+1)
        contMayusculas += 1
    elif elemento in vocales:
        posVocales.append(cont+1)
        contVocales += 1
    cont += 1

print (f"La cantidad de caracteres es: {len(frase)- contVacio}\n"
       f"La cantidad de consonantes es: {contConsonantes}\n"
       f"La cantidad de caracteres especiales es: {contEspeciales}\n"
        f"La cantidad de mayusculas es: {contMayusculas}\n"
        f"La posicion de las mayusculas es: {posMayusculas}\n"
        f"La cantidad de vocales es: {contVocales}\n"
        f"La posicion de las vocaless es: {posVocales}\n")