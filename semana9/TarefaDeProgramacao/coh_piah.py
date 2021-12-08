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


def separa_palavras(frase):
    '''A função recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)












































                       


