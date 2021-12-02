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

            if pecas_restantes == 0:
                vencedor = 0
                break
            # jogada computador
            pecas_retiradas = computador_escolhe_jogada(pecas_restantes, m)
            pecas_restantes = pecas_restantes - pecas_retiradas

            if pecas_restantes == 0:
                vencedor = 1
                break
        else: # caso que o computador começa a partida
            print("Computador começa!\n")
            while pecas_restantes > 0:

                # jogada computador
                pecas_retiradas = computador_escolhe_jogada(pecas_restantes, m)
                pecas_restantes = pecas_restantes - pecas_retiradas

                if pecas_restantes == 0:
                    vencedor = 1
                    break

                # jogada usuário
            pecas_retiradas = usuario_escolhe_jogada(pecas_restantes, m)
            pecas_restantes = pecas_restantes - pecas_retiradas

            if pecas_restantes == 0:
                vencedor = 0
                break
    if vencedor == 1:
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    elif vencedor == 0:
        print("Fim de jogo! O computador ganhou!\n")
        return 0




















                

        
 

    
