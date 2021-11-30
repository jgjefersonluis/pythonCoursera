def éPrimo(k):

    divisores = 0
    for i in range(1,k):
        if k % i == 0:
            divisores += 1
    if divisores >= 2:
        return False
    else:
        return True
