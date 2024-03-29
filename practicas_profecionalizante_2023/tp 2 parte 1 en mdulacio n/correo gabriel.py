

def validar_correo (correo):
    mensaje_error=[]

    #a) Caracteres permitidos
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
    for caracter in  correo:
        if caracter not in caracteres_permitidos:
            mensaje_error.append(f"Se ha ingresado un caracter invalido")

    # b) No se permiten espacios en blanco
    if ' ' in correo:
        mensaje_error.append(f"El correo contiene espacios")

    # c) El mail debe iniciar con una letra
    elif not correo[0].isalpha():
        mensaje_error.append(f"El correo no comienza con una letra ")

    #d) Longitud minima antes del @
    partes_correo= correo.split("@")

    if len(partes_correo) == 2:
        usuario,dominio = partes_correo

    elif len(usuario) < 5:
      mensaje_error.append(f"El usuario debe tener al menos 5 caracteres")

    #e) Debe contener un solo @
    if correo.count( "@") != 1:
        mensaje_error.append()
  
    #f) logitud minima del dominio
    if len(dominio) < 5:
      mensaje_error.append(f"El dominio debe tener al menos 5 caracteres")

    #f) Existencias de puntos al inicio y al final del dominio
    elif '.' in dominio:
        if dominio[0] == '.' or dominio[-1] == '.':
            mensaje_error.append(f"El dominio no puede comenzar ni terminar con un punto '.' ")
        if '@.' in dominio:
            mensaje_error.append(f"No puede ir un punto '.'  despues del '@' ")

    #g)Verificar que el dominio termine con al menos 3 caracteres despues del punto
    dominio_final= dominio.split('.')

    if len(dominio_final) ==2:
        primer_dominio, segundo_dominio = dominio_final
    elif len(segundo_dominio) < 3:
        mensaje_error.append(f"El formato debe contener al menos 3 caracteres")
    else:
        mensaje_error.append(f"El formato del correo es valido")
    
    return mensaje_error

#____ Programa Principal ______



#cantidad_de_correos = int(input("Ingrese la cantidad de correos para verificar: "))
# contador_correos=1

# while contador_correos <= cantidad_de_correos:
#   correo_electronico=input("Ingrese el correo para verificar: ")
#   verificacion_correo= validar_correo(correo_electronico)
#   contador_correos+=1
correo_electronico=input("Ingrese el correo para verificar: ")
verificacion_correo=validar_correo(correo_electronico)
print(f"El correo electronico {correo_electronico} en su validacion da como mensaje {verificacion_correo}")
