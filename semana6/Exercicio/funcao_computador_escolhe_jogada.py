# n = número de peças iniciais
# m = número máximo de peças a ser retiradas pelos jogadores

def computador_escolhe_jogada(n,m):
#caso que peças disponiveis é menor que o número
#máximo de peças que se pode tirar
    if n < m:
        print("O computador tirou %d peças." %n)
        print("Agora restam %d peças no tabuleiro.\n" % (n-n))
        proxima_jogada = n
#caso que o cpu calcula a quantidade de peças para retirar
    elif calcula_jogada(n,m) != 0:
        proxima_jogada = calcula_jogada(n,m)
        print("O computador tirou %d peças." % proxima_jogada)
        print("Agora restam %d peças no tabuleiro.\n" % (n-proxima_jogada))
#caso que o cpu retira o maior número de peças possíveis
    else:
        print("O computador tirou %d peças." % m)
        print("Agora restam %d peças no tabuleiro.\n" % (n-m))
        proxima_jogada = m

    return proxima_jogada

        
