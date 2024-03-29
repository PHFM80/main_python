import random
from os import system
from time import sleep

lista_nombres = ["Pablo", "Marcela", "Matias", "Andrea", "Emiliano", "Luciano", "Lucas", "Maria"]
lista_apellidos = ["Mora", "Flores", "Gonzalez", "Perez", "Gomes", "Murua", "Lopes", "Terrera", "kai"]
lista_calles = ["Mexico", "Marea Roja","Lagos Argentinos", "Barcelona", "Peru", "Chile", "Balcarce", "San Martin"]
lista_departamentos = ["Godoy Cruz", "Lujan", "Las Heras", "Maipu", "Junin", "Lavalle", "Ciudad", "Guaymallen", "Malargue"]




system ("cls")
while True:
    
    print ("================================\n"
       "\tMenu de datos\n"
       "================================\n")
    
    print ("1 Para generar nuevos datos.\n"
           "2 Para cargar los datos generados en la base de datos.\n"
           "3 Para salir del sistema.\n")
    opc = int(input("Ingrese una opcion:\n"))

    if opc == 1:
        nombre = random.choice(lista_nombres)
        apellido = random.choice(lista_apellidos)
        telefono = str(random.randint(1111111, 9999999))
        codigo = "261"
        celular = int(codigo+telefono)
        edad = random.randint(18, 99)
        num_casa = random.randint(111, 9999)
        calle = random.choice(lista_calles)
        departamento = random.choice(lista_departamentos)


        print (f"\n\t\tNombre: {nombre} \n\t\tApellido: {apellido} \n\t\tCelular: {celular} \tEdad: {edad}"
        f"\n\t\tCalle: {calle} N°: {num_casa}  Departamento: {departamento}\n")

    elif opc == 2:
        print ("Datos Cargados\n")
        sleep(2)
        system("cls")
    elif opc == 3:
        print ("Saliendo del sistema.\n")
        sleep(2)
        system ("cls")
        break
    else:
        print ("Ingrese una opcion correcta\n"
               "Solo se pueden ingresar numeros.")
        
//Como conecto a una base de datos mySql en workbench?