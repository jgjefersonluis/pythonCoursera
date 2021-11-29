x = input("Insira um número inteiro:")

tamanho = len(x)
valor_x = int(x)

soma = 0
restante = valor_x

for i in range(tamanho):
    soma += restante % 10
    restante = restante // 10
    
print('A soma dos caracteres é:', soma)
