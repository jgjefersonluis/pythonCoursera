preço = 24
item = "banana"
print("O preço do kilo de %s é %d reais"%(item,preço))

print("O preço do kilo de %+10s é %5.2d reais"%(item,preço))

print("O preço do kilo de %+10s é %10.2f reais"%(item,preço))

dicio = {"item":"banana","preço":24}
print("O preço do kilo de %(item)s é %(preço)7.1f reais"%dicio)
