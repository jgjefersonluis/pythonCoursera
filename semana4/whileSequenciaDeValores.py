print("Digite uma sequência de valores. Digite zero para finalizar.")

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor a ser somado:"))
    soma += valor
    
print("A soma dos valores digitados é:", soma)
