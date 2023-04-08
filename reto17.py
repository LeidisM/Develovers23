"""Desarrollar un algoritmo y ponerlo en funcionamiento que simule el juego de adivinar el número,

El algoritmo debe generar un número aleatorio entre 0 y 1000 y deberás ingresar números hasta que des con el número secreto

"""
import random

numero_adivinar=0

opcion_computador= random.randint(0,1000)

while opcion_computador != numero_adivinar:


    numero_adivinar = int(input("ingrese numero secreto"))
    if numero_adivinar > 1000 or numero_adivinar < 0:
        print("Numero ingresado está fuera de rango")
        numero_adivinar = int(input("ingrese numero"))
        print("El numero ingresado por el usuario es", numero_adivinar)

        if opcion_computador == numero_adivinar:
            print("Ganaste")
            break

        else:
            print("Sigue intentando")

print("Esta fue la opción del pc", opcion_computador)

print("Esta fue tu opción",numero_adivinar)
