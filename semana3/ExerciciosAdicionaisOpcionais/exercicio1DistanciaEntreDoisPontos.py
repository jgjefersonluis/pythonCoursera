import math

x1 = int(input("Insira o primeiro número inteiro, por favor: "))
y1 = int(input("Insira o primeiro número inteiro, por favor: "))
x2 = int(input("Insira o primeiro número inteiro, por favor: "))
y2 = int(input("Insira o primeiro número inteiro, por favor: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2)

if distancia >= 10:
    print("Longe")
else:
    print("Perto")
