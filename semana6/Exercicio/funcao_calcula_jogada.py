def calcula_jogada(n,m):
    pecas_a_retirar = 0

    for i in range(1,m+1):
        if(n-i)%(m+1) == 0: # caso que dá para retirar as peças!
            pecas_a_retirar = i
    return pecas_a_retirar

