decrescente = True

anterior = int(input("Digite o primeiro número da sequência: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número (inteiro) da sequência (digite zero para sair): "))
    if valor > anterior:
        decrescente = False
    anterior = valor
    
if decrescente:
    print("A sequência está em ordem decrescente! =D")
else:
    print("A sequência não está em ordem descrescente! :-(")
