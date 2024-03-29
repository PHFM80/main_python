import datetime as dt

def hora():
    hoy = dt.datetime.today() 
    horaActual = hoy.strftime("%H:%M:%S")
    return horaActual
def fecha():
    hoy = dt.datetime.today()
    fechaActual = hoy.strftime("%d-%m-%y")
    return fechaActual



#Creacion de 3 salas de cine
sala1 = []
sala2 = []
sala3 = []

for i in range(20):
    sala1.append (["O"]*20)
    sala2.append (["O"]*15)
for i in range(13):
    sala3.append (["O"]*13)

#llenado del pasillo de la sala 1
for i in range (20):
    for j in range (20):
        sala1[i][4] = "P"
        sala1[i][-5] = "P"

# impresion de la sala 1
print ("SALA 1\n")
for i in sala1:
    print (" ")
    for j in i:
        print (j, end="  ")

#llenado del pasillo de la sala 2
for i in range (20):
    for j in range (15):
        sala2[i][3] = "P"
        sala2[i][7] = "P"
        sala2[i][-4] = "P"

# impresion de la sala 2
print ("\nSALA 2\n")
for i in sala2:
    print (" ")
    for j in i:
        print (j, end="  ")

#llenado del pasillo de la sala 3
for i in range (12):
    for j in range (12):
        sala3[i][6] = "P"

# impresion de la sala 3
print ("\nSALA 3\n")
for i in sala3:
    print (" ")
    for j in i:
        print (j, end="  ")





