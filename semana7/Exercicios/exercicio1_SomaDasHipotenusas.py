def soma_hipotenusas(n): # para ver os valores das hipotenusas
    
    lista = []
    soma = 0
    
    for i in range(2, n+1):
        if é_hipotenusa(i) == True:
            lista.append(i)
            soma += i

    print(lista)
    print(soma)
