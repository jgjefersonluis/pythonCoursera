def remove_repetidos(lista):
    
    lista_aux = []
    
    for i in lista:
        if i not in lista_aux:
            lista_aux.append(i)
    
    lista_aux.sort()
    
    return lista_aux

lista = [10, 1, 2, 3, 4, 5, 2, 6, 7, 4, 3, 8, 9]
remove_repetidos(lista)

lista = [4, 3, 6, 2, 1, 5]
lista.sort()
lista

print (lista)
