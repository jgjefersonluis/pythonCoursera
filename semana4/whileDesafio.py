x = input('Insira um valor inteiro:')

tamanho = len(x)
verifica = False
i = 0

while i < tamanho - 1:
    if x[i] == x[i + 1]:
        verifica = True
    i += 1
    
if verifica:
    print("Este número contém dois caracteres adjacentes iguais.")
else:
    print("Este número NÃO contém dois caracteres adjacentes iguais.")
