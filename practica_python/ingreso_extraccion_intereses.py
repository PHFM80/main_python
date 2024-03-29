from os import system
from time import sleep

cont = 0
print ("Calcularemos la tasa de interes mensual en base a la tasa Nominal anual.  "
       "Para eso deberemos ingresar los siguientes datos.")
tna = float(input("Ingrese la Tasa de Interes Anual (TNA): "))
cantMes = int(input("Ingrese la cantida de meses que va a establecer el plazo fijo: "))

interes1 = 0
capital = 0

#tnm es la tasa nominal mensual.  se calcula dividiendo la TNA en 12 meses
tnm = (tna/12)/100
system ("cls")


while True:
    if cont == cantMes:
        print ("Llego a la cantida de meses estipulados para calcular el plazo fijo.\n")
        sleep(4)
    system ("cls")
    opc = int(input("Ingrese la opcion que desea realizar: \n"
                    "1_ Para realizar un deposito.\n"
                    "2_ Para realizar una extraccion.\n"
                    "3_ Para ver los interese del mes.\n"
                    "4_ Para avanzar al siguiente mes.\n"
                    "5_ Para salir del programa.\n"))

    if opc == 1:
        system("cls")
        print ("\nMenu de deposito.\n")
        monto = int(input(f"Ingrese la suma de dinero a depositar el mes {cont}: \n"))
        capital = capital + monto

    elif opc == 2:
        system("cls")
        print ("\nMenu de extracción.\n")
        retiro = int(input(f"Ingrese la suma de dinero que desea retirar: \n"))
        if capital > retiro: 
            capital = capital - retiro
        elif retiro > capital:
            print ("No se puede retirar mas dinero que se tiene en el capital")

    elif opc == 3:
        print (f"El total depositado mas los intereses generados del mes anterior es: {round(capital,2)}")
        print (f"Los intereses generados del mes anterior es: {round(interes1, 2)}")
        sleep(4)
        
    elif opc == 4:
        interes = tnm * monto
        interes1 = interes1 + interes
        capital = capital + interes
        cont += 1

    elif opc == 5:
        print ("Saliendo del programa")
        
        sleep(3)
        system ("cls")
        break

    else:
        print ("Opcion incorrecta\n"
               "Ingrese una opcion correcta.")
        system ("cls")




# for i in range(0, cantMes+1):
#     print(". . . . . . . . . . . .")
#     print(f"Para el mes {i}, el capital es ${round(capital, 2)}")
#     print(f"La tasa nominal mensual es de: ${round(tnm, 4)}")
#     interes = monto * tnm
#     monto = monto + interes
#     print(f"Los intereses del mes son de: ${round(interes, 2)}")
#     print(f"El monto a retirar es de: ${round(monto, 2)}")
#     print(". . . . . . . . . . . .")

# print(f"El monto final es de ${round(monto, 2)}")
