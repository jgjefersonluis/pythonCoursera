def usuario_escolhe_jogada(n,m):

    jogada_usuario = int(input("Informe sua jogada: "))

    while jogada_usuario <= 0 or jogada_usuario > n or jogada_usuario > m:
        print("Valor incorreto. O valor deve estaru entre 1 e %d, ou ser menor que a quantidade de peças disponíveis (%d)" % (n,m))
        jogada_usuario = int(input("Informe sua jogada: "))

    print("\nVocê tirou %d peças." % jogada_usuario)
    print("Agora resta %d peças no tabuleiro.\n" % (n-jogada_usuario))
    return jogada_usuario


    
