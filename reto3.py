"""Escribir un algoritmo que reciba una x cantidad de números y los devuelva organizados ascendente y descendentemente.
En caso de existir números repetidos sólo deberá mostrar uno.
Ejemplo: 1 9 5 7 9 3 1
Salida:

1 3 5 7 9
9 7 5 3 1"""



long = int (input("Cuantos numeros desea ingresar: "))
numbers = []
for x in range(long):
    valor=int(input("Ingrese un numero: "))
    numbers.append(valor)
for valor in numbers:
    list_uniq=list(set(numbers))
    list_uniq.sort()
print(list_uniq)
    deso= sorted(list_uniq,reverse=True)
print(deso)