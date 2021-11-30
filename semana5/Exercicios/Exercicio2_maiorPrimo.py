def maior_primo(n):
    
    maior_primo = 1
    
    for i in range(n + 1):
        if éPrimo(i) == True:
            maior_primo = i
    
    return maior_primo
