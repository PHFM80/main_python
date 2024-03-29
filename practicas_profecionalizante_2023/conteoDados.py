# conteo = 0
# tiradas = 0
# for dado1 in range(1, 7):
#     for dado2 in range(1 , 7):
#         for dado3 in range(1, 7):
#             tiradas += 1
#             #print (f"Tirada n° {tiradas}: dado1 = {dado1}, dado2 = {dado2}, dado3 = {dado3}")
#             if dado1 + dado2 + dado3 == 10:
#                 conteo += 1
#                 #print (f"Forma n° {conteo}: dado1 = {dado1}, dado2 = {dado2}, dado3 = {dado3}")
# print (f"El total de tiradas que se pueden lograr es n° {tiradas}")  
# print (f"El total de formas que se pueden lograr es n° {conteo}")
# casosFavorables = conteo
# numeroCasos = tiradas
# prob10 = casosFavorables/numeroCasos
# probCadaTres = round((3 * prob10 - 3 * (pow(prob10, 2)) + pow (prob10, 3))*100 , 2)
# #probCadaTres = round(probCadaTres*100, 2)
#print (f"La probabilidad de tener un 10 cada 3 tiradas es de: {probCadaTres}%")

# tiradas1 = 0
# dado1 = [1, 2, 3, 4, 5, 6]
# dado2 = [1, 2, 3, 4, 5, 6]
# dado3 = [1, 2, 3, 4, 5, 6]
# conteo1 = 0 
# for i in dado1:
#     for j in dado2:
#         for l in dado3:
#             tiradas1 += 1
#             print (f"Tirada n° {tiradas1}: dado1 = {i}, dado2 = {j}, dado3 = {l}")
#             if i + j + l == 10:
#                 conteo1 += 1
#                 print (f"Forma n° {conteo1}: dado1 = {i}, dado2 = {j}, dado3 = {l}")
# print (f"El total de tiradas que se pueden lograr es n° {tiradas1}")                
# print (f"El total de formas que se pueden lograr es n° {conteo1}")


# 4) desarrolle un programa que pregunte al usuario si desea encontrar el numero mas grande o el
# mas chico de una serie de numeros ingresados por teclado.  y efectivamente el programa devolvera 
# el mas grande o el mas chico de todos los numeros ingresados

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


