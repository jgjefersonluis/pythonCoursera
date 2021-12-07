import re

def le_assinatura():

    '''A função le os valores dos traços linguisticos do modelo e devolve uma assinatura a
    ser comparada com os textos forneciodos'''
    print("Bem vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))

    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))

    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]
                       


