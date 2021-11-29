tamanho = int(input("Digite o tamanho da sequência de números:"))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado ao anterior (faltam %d números):" % (tamanho - i)))
    produto *= valor
    i += 1
    
print("A multiplicação dos valores digitados é:", produto)
