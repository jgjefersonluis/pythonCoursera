def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada?"))

    vencedor = 2 # variável de ocntrole para quem venceu. 1 para cpu, 0 para usuário.

    pecas_restantes = n

    if n % (m + 1) == 0: # caso que o computador deixa o usuário começar
        print("Você começa!\n")
        proxima_jogada = 0

        while pecas_restantes > 0:
            # jogada usuário
            pecas_retiradas = usuario_escolhe_jogada(pecas_restantes, m)
            pecas_restantes = pecas_restantes - pecas_retiradas

            

    
