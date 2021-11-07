x = float(input("Digite um numero: "))
if x < 0:
    print(x, "< 0")
elif x == 0:
    print(x, "== 0")
elif x < 1:
    print("0 < ", x,"< 1")
elif x < 2:
    print("1 <=", x, "< 2")
elif x < 3:
    print("2 <=", x, "< 3")
elif x < 5:
    print("3 <=", x, "< 5")
else:
    print("5 <=", x)

print("Termino do teste.")
