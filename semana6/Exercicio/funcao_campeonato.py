def campeonato():

    rodada = 1

    partidas_ganhas_cpu = 0
    partidas_ganhas_usuario = 0

    while rodada <= 3 :
        print("**** Rodada %d ****" % rodada)
        vencedor = partida()
        if vencedor == 1:
            partidas_ganhas_cpu += 1
        elif vencedor == 0:
            partidas_ganhas_usuario += 1
        rodada += 1

    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d x %d Computador" % (partidas_ganhas_usuario, partidas_ganhas_cpu)) 
