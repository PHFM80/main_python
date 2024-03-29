#a) Caracteres permitidos
def caracteres_permitidos(correo):    
    validar_caracter = True
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
    for caracter in  correo:
        if caracter not in caracteres_permitidos:
            validar_caracter = False
            print (f"Se ha ingresado un caracter invalido\n")
            
    return validar_caracter

# b) No se permiten espacios en blanco
def espacios_blancos (correo):
    validar_espacio_blanco = False
    if ' ' in correo:
        print (f"El correo contiene espacios\n")
    else:
        validar_espacio_blanco = True
    return validar_espacio_blanco

# c) El mail debe iniciar con una letra
def comienza_letra(correo):
    letraInicial = True
    if not correo[0].isalpha():
        (f"El correo no comienza con una letra \n")
        letraInicial = False
    return letraInicial

#d) Longitud minima antes del @
def longitud_usuario(correo):
    largoUsuario = True
    contUsuario = 0
    for i in correo:
        if i != "@":
            contUsuario += 1
        else:
            break

    if contUsuario < 5:
        print (f"El usuario debe tener al menos 5 caracteres\n")
        largoUsuario = False
    return largoUsuario

#e) Debe contener un solo @
def contador_arroba(correo):
    contArroba = True
    if correo.count( "@") != 1:
        print ("El correo debe tener solo un @\n")
        contArroba = False
    return contArroba

# funcion para crear el dominio
def func_dominio(correo):
    #determina el dominio sin el arroba, el contador comienza en 1 para asi sumar 
        # el arroba y dejar el dominio limpio
    largoUsuario = 1        
    for i in correo:
        if i != "@":
            largoUsuario += 1
        else:
            break
    dominio = correo[largoUsuario : len(correo)]
    return dominio

#f) Existencias de puntos al inicio y al final del dominio
def puntos_dominio(correo):
    verificarPuntos = False
    dominio = func_dominio(correo)
        #determina que halla un solo punto en el dominio
    contPuntos = 0
    for i in correo:
        if i == ".":
            contPuntos += 1
    if contPuntos != 1:
        print ("El domininio debe tener un solo punto.\n")
    else:
        #determina que el dominio no comienze ni termine con punto
        if dominio[0] == '.' or dominio[-1] == '.':
            print (f"El dominio no puede comenzar ni terminar con un punto '.' \n")
        else:
            verificarPuntos = True
    return verificarPuntos

#g)Verificar que el dominio termine con al menos 3 caracteres despues del punto
def fin_tres_caracteres(correo):
    dominio = func_dominio(correo)
    largoPostunto = False
    if dominio[-4] != ".":
        print ("Deben haber 3 caracteres despues del punto\n")
    else:
        largoPostunto = True
    return largoPostunto


#____ Programa Principal ______

correo_electronico=input("Ingrese el correo para verificar: \n")

caracterValido = caracteres_permitidos(correo_electronico)
espacioBlanco = espacios_blancos(correo_electronico)
letraInicial = comienza_letra(correo_electronico)
longitudUsuario = longitud_usuario(correo_electronico)
cantArroba = contador_arroba(correo_electronico)
puntosDominio = puntos_dominio(correo_electronico)
finTresCaracteres = fin_tres_caracteres(correo_electronico)


#estos print son para verificar lo que te devuelven las funciones
# print (f"esto es un caracter valido = {caracterValido}")
# print (f"estos es un espacio en blanco = {espacioBlanco}")
# print (f"estos es la letra inicial = {letraInicial}")
# print (f"esta es la longitud del usuario = {longitudUsuario}")
# print (f"esta es la cantidad de arrobas = {cantArroba}")
# print (f"esta es la verificacion de puntos en el dominio = {puntosDominio}")
# print (f"esta es la verificacion del 3 caracteres post punto = {finTresCaracteres}")

#en este condicional se verifca si el correo es valido o no
if caracterValido == True and espacioBlanco == True and letraInicial == True and longitudUsuario == True and cantArroba == True and puntosDominio == True and finTresCaracteres == True:
    print (f"El correo: {correo_electronico}, es valido.\n")
else:
    print (f"El correo: {correo_electronico}, NO es valido.\n")
