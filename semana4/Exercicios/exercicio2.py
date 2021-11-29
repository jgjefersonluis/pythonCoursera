quantidade = int(input("Insira um número inteiro positivo:"))

i = 1

while quantidade > 0:
    if i % 2 != 0:
        print(i)
        quantidade -= 1
    i += 1
