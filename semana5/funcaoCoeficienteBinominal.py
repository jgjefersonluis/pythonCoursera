def coeficiente_binomial(n,k):

    def fat(x):
        
        if x<=1:
            return 1
        else:
            return x*fat(x-1)

    numerador = fat(n)
    denominador = fat(x) * fat(n-k)

    return numerador // denominador

    print (coeficiente_binomial(4, 2))
    print (coeficiente_binomial(10, 3))
