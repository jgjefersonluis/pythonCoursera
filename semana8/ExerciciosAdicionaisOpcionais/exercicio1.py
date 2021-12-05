def maior_elemento(lista):
    
    maior = lista[0]
    
    for i in lista:
        if maior < i:
            maior = i
    
    return maior

lista = [4, 3, 6, 2, 1, 5]
maior_elemento(lista)

print(maior_elemento(lista))

maior_elemento([-90, -27, -12])

print(maior_elemento(lista))
