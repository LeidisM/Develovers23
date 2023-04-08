"""Desarrollar un algoritmo que capture 13 números, y de ellos:

- obtener y mostrar el mayor
- obtener y mostrar el menor
- obtener y mostrar la suma de todos
- obtener y mostrar el promedio
- mostrar los repetidos
"""

numeros = []
iterador = 0

#ingreso de n numeros
while iterador < 13:
    num= int(input(" Ingrese el numero "))
    numeros.append(num)
    iterador=iterador+1
#print("Soy todos los numeros del array", numeros)

#repetidos mostrar
veces = 0
repetidos = []

#mayor
mayor = 0

for i in (numeros):
    if i > mayor:
    mayor = i

print("Soy el mayor: ", mayor)

#Menor
menor = numeros[0]

for j in (numeros):
    if j < menor:
    menor = j

print("Soy el menor: ", menor)

#Suma
suma = 0

for k in (numeros):
    suma=suma+k

print("Soy la suma", suma)

#Promedio
longitud = (len(numeros))
print("soy el promedio",suma/longitud)

#Soy los numeros repetidos del array
for a in numeros:
    veces = 0
for b in numeros:
    if a == b:
    veces+=1
if veces > 1:
    repetidos.append(a)

print("Soy los numeros que estan repetidos", repetidos)