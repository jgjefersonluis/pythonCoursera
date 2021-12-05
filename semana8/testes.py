'''
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")


carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")

carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1

print (carnes1)
print (carnes2)
print (carnes3)
'''

pares = [2, 4, 6, 8, 10]
x = pares * 3

#print (pares)
print(x)
