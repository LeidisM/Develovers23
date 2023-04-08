""Desarrollar un algoritmo que reciba un número entero y lo convierta a binario y hexadecimal.
""


dividendo= int (input("ingresa un numero a convertir en binario "))
binario = []
while dividendo > = 1:
    binario.append(dividendo%2)
    dividendo=int(dividendo/2)
    log = len(binario)-1
inver = []

for i in range(1, len(binario)+1, 1):
    inver.append(binario[-i])
print(inver)


hexadecimal = []
numero = int (input("ingresa un numero a convertir a hexadecimal==>"))

while numero > 1:
    hexadecimal.append(numero%16)
    numero = int(numero/16)
    longitud = len(hexadecimal)-1

dicHexadecimal = {
0:0,
1:1,
2:2,
3:3,
4:4,
5:5,
6:6,
7:7,
8:8,
9:9,
10:"A",
11:"B",
12:"C",
13:"D",
14:"E",
15:"F"}

invertido=[]
for i in range(1, len(hexadecimal)+1, 1):
    invertido.append(hexadecimal[-i])

resultadHexa = []

for resultad in invertido:
    resultadHexa.append(invertido[-i])
print(dicHexadecimal[resultad])
