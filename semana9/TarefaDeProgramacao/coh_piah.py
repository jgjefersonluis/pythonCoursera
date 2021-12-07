import re

def le_assinatura():

    '''A função le os valores dos traços linguisticos do modelo e devolve uma assinatura a
    ser comparada com os textos forneciodos'''
    print("Bem vindo ao detector automático de COH-PIAH.")

    wal=float(input("Entre o tamanho medio de palavra: "))
    ttr=float(input("Entre a relação Type-Token: "))
    hlr=float(input("Entre a Razão Hapax Legomana: "))
    sal=float(input("Entre o tamanho médio de sentença: "))
    sac=float(input("Entre a complexidade média da sentença: "))
    pal=float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i=1
    textos=[]
    texto=input("Digite o texto"+str(i)+"(aperte enter para sair):")
    while texto:
        textos.append(texto)
        i+=1
        texto=input("Digite o texto"+str(i)+"(aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funçao recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas=re.split(r'[.!?]+',texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentencas):
    '''A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return frase.split()












































                       


