"""Desarrollar y poner en funcionamiento un algoritmo que genere 100 números aleatorios del 0 al 99, y concatenarlo en un solo. Por ejemplo:

Aleatorios:

32,45,78,23,90,1,3,89……

Resultado
32457823901389

Una vez generado el aleatorio gigante, solicitar ingresar un número cualquiera entre 0 y 99, e indicar si existe o no en el el. Por ejemplo, tomando el número anterior:

Ingresa el 39, el algoritmo imprime OK
"""
import random
arrays_numeros_completos = []

for i in range(100):
    numeros = str(random.randint(0, 99))
    arrays_numeros_completos.append(numeros)
#print(numeros)
#print(arrays_numeros_completos)

convertidor = ''.join(arrays_numeros_completos)
    print(convertidor)

numero_buscado = str(input("Ingrese el numero a buscar"))

for j in arrays_numeros_completos:
    if numero_buscado in arrays_numeros_completos:
    print("ok")
