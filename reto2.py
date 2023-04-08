#Escribir, desarrollar y poner en funcionamiento un algoritmo que sume todos los números pares en un rango especificado, por ejemplo:
#Rango: 4 - 15, resultado: 54
#Rango: 1 - 7, resultado: 12

range_ini = int(input("Ingrese el numero de rango inicial =>"))
range_fin = int(input("Ingrese el numero de rango final =>"))
sum3=0
for i in range (range_ini,range_fin+1):
    if i % 2==0:
    sum3+= i
print(sum3)