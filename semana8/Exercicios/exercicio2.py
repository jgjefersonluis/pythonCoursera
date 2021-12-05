def soma_elementos(lista):
    soma = 0

    for i in lista:
        soma += i
    return soma

lista = [4, 3, 6, 2, 1, 5]
soma_elementos(lista)

print(soma_elementos(lista))
