import datetime as dt

def hora():
    hoy = dt.datetime.today() 
    horaActual = hoy.strftime("%H:%M:%S")
    return horaActual
def fecha():
    hoy = dt.datetime.today()
    fechaActual = hoy.strftime("%d-%m-%y")
    return fechaActual

saldo = 0
cont_id = 0

columnas = 5

cajero = []


cajero.append (["ID", "Monto ", "Fecha", "   Hora", "  transaccion"])
    

while True:

    try:
        print ("\n\t\tBienvenido al Cajero Automatico.\n")
        opc = int (input("Menu del cajero:\n"
                        "\t1. Realizar un deposito en la cuenta.\n"
                         "\t2. Realizar un retiro de la cuenta.\n"
                          "\t3. Ver los movieminetos de la cuenta.\n"
                           "\t4. Salir del cajero.\n" 
                           f"\t\t\t\t\tEl saldo en la cuenta es: ${saldo} \n"))
        
        if opc == 1:
            cont_id += 1
            monto = float(input("Ingrese el monto que desea depositar: \n"))
            print ("")
            if monto > 0:
                saldo += monto
                cajero.append ([cont_id, monto, fecha(), hora(), "Deposito"])
                print (f"Transaccion n°: {cont_id}, acaba de realizar un deposito, "
                   f"el monto es: {monto}, hoy es: {fecha()} son las {hora()}")

            else:
                print ("Ingrese un saldo mayor a 0\n")
                

        elif opc == 2:
            monto = float(input("Ingrese el monto que desea extraer: \n"))
            if saldo > monto:
                cont_id += 1
                saldo -= monto
                cajero.append ([cont_id, monto, fecha(), hora(), "Extraccion"])
                print (f"Transaccion n°: {cont_id}, acaba de realizar una extracción, "
                   f"el monto es: {monto}, hoy es: {fecha()} son las {hora()}")
                
            else:
                print ("El monto que desea extraer supera el saldo.")
        
        elif opc == 3:
            for i in range(len(cajero)):
                print ("")
                for j in range(columnas):
                    print (cajero[i][j], end="   ")


        elif opc == 4:
            print ("\nSaliendo del programa...\n")
            break

        else:
            print ("Usted debe ingresar una opcion correcta.\n")
    except ValueError:
        print ("Usted ingreso una letra.\nDebe Ingresar solo números.\n")