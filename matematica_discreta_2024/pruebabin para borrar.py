# CONVERTIR A DECIMAL
#numBInario = "101010"
# print (numBInario)
# numBInario = numBInario[::-1]
# print (numBInario)
# acum = 0
# cont = 1
# cont1 = 1
# for i in numBInario:
#     print (f"esta es la posicion {cont1}, y es el digito {i}")
#     if i == "0":
#         acum += 0
#         print (f" este es el acumulador : {acum}")
#         cont = cont * 2
#         cont1 += 1
#     elif i == "1":
#         print (f"este es el contador {cont}")
#         acum += cont
#         print (acum)
#         cont = cont * 2
#         cont1 += 1

# print (f"la acumulacion final es: {acum}")

# numBInario = "1010"
# print (numBInario)
# numBInario = numBInario[::-1]
# print (numBInario)
# acum = 0
# cont = 1
# cont1 = 1
# for i in numBInario:
#     print (f"esta es la posicion {cont1}, y es el digito {i}")
#     if i == "0":
#         print (f"esto es lo que suma {cont*0}")
#         acum += cont *0
#         print (f" este es el acumulador : {acum}")
#         cont = cont * 2
#         cont1 += 1
#     elif i == "1":
#         print (f"esto es lo que suma {cont}")
#         acum += cont
#         print (f" este es el acumulador : {acum}")
#         cont = cont * 2
#         cont1 += 1
#     print ("")

# print (f"la acumulacion final es: {acum}")

# CONVERTIR A OCTAL

# numBinario = "1011011"
# print (numBinario)
# numBinario = numBinario[::-1]

# # Inicializamos una lista para almacenar los conjuntos de tres caracteres
# conjuntos = []

# # Iteramos sobre el numero binario (numBinario) tomando grupos de tres caracteres
# for i in range(0, len(numBinario), 3):
#     conjunto = numBinario[i:i+3]  # Tomamos un conjunto de tres caracteres
#     conjuntos.append(conjunto)  # Agregamos el conjunto a la lista

# print(conjuntos)

# # Aca convertimos a decimal y en cada iteracion de la lista conjuntos convertimos a decimal y lo agregamos a una nueva lista

# decimal = []

# for num in conjuntos:
#     acum = 0
#     cont = 1
#     cont1 = 1
#     for i in num:
#         print (f"esta es la posicion {cont1}, y es el digito {i}")
#         if i == "0":
#             print (f"esto es lo que suma {cont*0}")
#             acum += cont *0
#             print (f" este es el acumulador : {acum}")
#             cont = cont * 2
#             cont1 += 1
#         elif i == "1":
#             print (f"esto es lo que suma {cont}")
#             acum += cont
#             print (f" este es el acumulador : {acum}")
#             cont = cont * 2
#             cont1 += 1
#         print ("")

#     print (f"la acumulacion final es: {acum}")
#     decimal.append(acum)
# print (decimal)

# # Invertir la lista
# lista_invertida = list(reversed(decimal))

# # Concatenar las cadenas
# cadena_concatenada = ''.join(str(x) for x in lista_invertida)

# print(cadena_concatenada)


#CONVERTIR A HEXADECIMAL


numBinario = "1011011"
print (numBinario)
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

