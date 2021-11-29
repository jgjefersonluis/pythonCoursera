meuCartão = int(input("Digite o número do seu cartão de crédito: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

# permanece no while enquanto o caracter não for zero ou não encontrou o número do cartão na lista
while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("Digite o número do próximo cartão: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("Encontrei!")
else:
    print("Não encontrei.")
