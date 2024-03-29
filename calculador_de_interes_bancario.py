print ("Calculador de Interteses Bancarios.\n")

cont = 0
tasaAnual = int(input("Ingrese la tasa de interes anual.\n"))

tasaMensual = tasaAnual/12
print (f"Tasa de interes = {tasaMensual}")
capital = 0

cantMeses = int(input("Ingrese la canidad de meses a calcular.\n"))

while cont !=cantMeses:
    print (f"El total de dinero en su cuenta es de: {capital}")

    interes = capital * tasaMensual / 100
    capital = interes + capital
    
    monto = int(input("Ingrese un monto de dinero:\n"))
    capital = capital + monto
    cont += 1




