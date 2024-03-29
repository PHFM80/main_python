
#### Funcion verificadora de numero binario
def verificar_binario (numBinario):
    es_binario = True
    largo = True
    numBin = False
    if len(numBinario) > 16:
        largo = False

    if largo == True:
        for digit in numBinario:
            if digit not in ('0', '1'):
                es_binario = False

    if largo == False:
        mensaje = "El número ingresado no cumple los 16 bits maximos."
    elif es_binario == False:
        mensaje = "El número ingresado no es binario"
    elif largo == True and largo == True:
        mensaje = "El número ingresado es binario y cumple los 16 bits de largo."
        numBin = True
    
    return mensaje,numBin

#### Funcion para convertir en decimal
def convertir_decimal(numBinario):
    numBinario = numBinario[::-1]
    print (numBinario)
    acum = 0
    cont = 1
    cont1 = 1
    for i in numBinario:
        print (f"esta es la posicion {cont1}, y es el digito {i}")
        if i == "0":
            print (f"esto es lo que suma {cont*0}")
            acum += cont *0
            print (f" este es el acumulador : {acum}")
            cont = cont * 2
            cont1 += 1
        elif i == "1":
            print (f"esto es lo que suma {cont}")
            acum += cont
            print (f" este es el acumulador : {acum}")
            cont = cont * 2
            cont1 += 1
        print ("")
    return acum

#### Funcion para convertir binario a octal
def convertir_octal (numBinario):
    numBinario = numBinario[::-1]

    # Inicializamos una lista para almacenar los conjuntos de tres caracteres
    conjuntos = []

    # Iteramos sobre el numero binario (numBinario) tomando grupos de tres caracteres
    for i in range(0, len(numBinario), 3):
        conjunto = numBinario[i:i+3]  # Tomamos un conjunto de tres caracteres
        conjuntos.append(conjunto)  # Agregamos el conjunto a la lista

    print(conjuntos)

    # Aca convertimos a decimal y en cada iteracion de la lista conjuntos convertimos a decimal y lo agregamos a una nueva lista

    decimal = []

    for num in conjuntos:
        acum = 0
        cont = 1
        cont1 = 1
        for i in num:
            print (f"esta es la posicion {cont1}, y es el digito {i}")
            if i == "0":
                print (f"esto es lo que suma {cont*0}")
                acum += cont *0
                print (f" este es el acumulador : {acum}")
                cont = cont * 2
                cont1 += 1
            elif i == "1":
                print (f"esto es lo que suma {cont}")
                acum += cont
                print (f" este es el acumulador : {acum}")
                cont = cont * 2
                cont1 += 1
            print ("")

        print (f"la acumulacion final es: {acum}")
        decimal.append(acum)
    print (decimal)

    # Invertir la lista
    lista_invertida = list(reversed(decimal))

    # Concatenar las cadenas
    cadena_concatenada = ''.join(str(x) for x in lista_invertida)

    print(cadena_concatenada)
    return cadena_concatenada
#### FUNCION PARA CONVERTIR BINARIO A HEXADECIMAL

def convertir_hexa(numBinario):
    numBinario = numBinario[::-1]

    # Inicializamos una lista para almacenar los conjuntos de tres caracteres
    conjuntos = []

    # Iteramos sobre el numero binario (numBinario) tomando grupos de tres caracteres
    for i in range(0, len(numBinario), 4):
        conjunto = numBinario[i:i+4]  # Tomamos un conjunto de cuatro caracteres
        conjuntos.append(conjunto)  # Agregamos el conjunto a la lista

    print(conjuntos)

    # Aca convertimos a decimal y en cada iteracion de la lista conjuntos convertimos a decimal y lo agregamos a una nueva lista

    hexa = []

    for num in conjuntos:
        acum = 0
        cont = 1
        cont1 = 1
        for i in num:
            print (f"esta es la posicion {cont1}, y es el digito {i}")
            if i == "0":
                print (f"esto es lo que suma {cont*0}")
                acum += cont *0
                print (f" este es el acumulador : {acum}")
                cont = cont * 2
                cont1 += 1
            elif i == "1":
                print (f"esto es lo que suma {cont}")
                acum += cont
                print (f" este es el acumulador : {acum}")
                cont = cont * 2
                cont1 += 1
            print ("")

        print (f"la acumulacion final es: {acum}")
        hexa.append(acum)
    print (hexa)
    numhexa = []
    # Invertir la lista
    lista_invertida = list(reversed(hexa))

    for i in lista_invertida:
        if i <= 9:
            numhexa.append(i)
        elif i == 10:
            numhexa.append("A")
        elif i == 11:
            numhexa.append("B")
        elif i == 12:
            numhexa.append("C")
        elif i == 13:
            numhexa.append("D")
        elif i == 14:
            numhexa.append("E")
        elif  i == 15:
            numhexa.append("F")
    print (numhexa)

    # Concatenar las cadenas
    cadena_concatenada = ''.join(str(x) for x in numhexa)

    print(cadena_concatenada)
    
    return cadena_concatenada





print (f"\t\tBienvenido al Programa de intercambio de sistemas númericos.")
print (f"\nEste programa te permitirá convertir un numero binario de 16bits, "
       f"a su representación en decimal, octal y hexadecimal.")
print (f"\nPara ello usted debe ingresar el número binario de 16 bits máximo (un máximo de 16 caracteres)") 

numBin = False
while numBin == False:
    numBinario = str(input("\nIngrese el número binario a convertir: ")) 
    # Comprobar que el número es correcto. Si no lo es mostrar mensaje de error e intentarlo nuevamente.

    mensaje, numBin = verificar_binario (numBinario)
    print (mensaje)
    print (numBin)

# Convertir Binario a Decimal

numDecimal = convertir_decimal(numBinario)
print (numDecimal)

# Convertir Binario a Octal
numOctal = convertir_octal(numBinario)
print (numOctal)

# Convertir Binario a Hexadecimal
numHexa = convertir_hexa(numBinario)
print (numHexa)

# Mostrando los resultados juntos
print (f"El número en binario ingresado es: {numBinario}\n"
       f"El número convertido a decimal con la funcion es: {numDecimal}\n"
       f"El número convertido a octal con la funcion es: {numOctal}\n"
        f"El número convertido a hexadecimal con la funcion es: {numHexa}\n")