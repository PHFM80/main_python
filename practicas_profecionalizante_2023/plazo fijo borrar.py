tasaMensual = 0.098
acumTotal = 0
acumSueldo = 0
totMeses = 15
contMes = 0
extracc = 0
# 2772592
#1891843
while contMes <= totMeses:
    print (f"El saldo inicial del mes es: {round(acumTotal, 2)}")
    interes = acumTotal * tasaMensual
    try:
        ingreso = int (input(f"Ingrese el dinero del mes {contMes} :     "))
        extraccion = int (input(f"Ingrese el dinero a extraer del mes {contMes} :     "))
    except ValueError:
        pass
    acumTotal += interes + ingreso - extraccion
    acumSueldo += ingreso
    contMes += 1
    extracc += 1
    print (f"El total de sueldo acumulado es de: ${acumSueldo}")
    print ("- - - - - - - - - - - - - - - - - - - - - - - - ")
    print (f"El interes generado en el mes {contMes}, es de: $ {round(interes, 2)}")
    print ("- - - - - - - - - - - - - - - - - - - - - - - - ")
    print (f"El saldo final del mes es: {round(acumTotal,2)}\n")
