def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")

    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        
