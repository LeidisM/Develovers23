"""Desarrollar un algoritmo que simule la descomposición numérica
Ejemplo:
60|2
30|2
15|2
5 |5
1 |

Recibirá un número de 1 a n , En este caso 60
Y deberá mostrar como resultado algo como:

60-30-15-5-1
2-2-3-5
"""


number = int(input("Ingrese el numero a descomponer=> "))
resultado= []
divis=[]
resultado.append(number)
divisor = 1

while (number != 1):
    divisor+=1

if number % divisor == 0:
    div = (number / divisor)

    number = div
    resultado.append(div)
    divis.append(divisor)
    divisor = 1

print(divis)

print(resultado)