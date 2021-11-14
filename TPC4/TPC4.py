#!/usr/bin/env python
# coding: utf-8

# # TPC 5

# # Frações

# ### data de início: 2021-10-27
# ### data de fim: 2021-11-07
# ### supervisor: José Carlos Ramalho
# ### autor: Filipa Pinho Serra Campos, a95303

# Resumo: Começou-se por criar um menu onde o utilizador pode escolher uma de várias funções disponíveis. De seguida foram criadas essas funções, das quais, várias permitem realizar operações aritméticas entre duas funções pedidas ao utilizador, através da função criarFracao(). Foram ainda criadas opções de frações em listas, podendo realizar-se a operação somar lista, que soma todos os elementos da lista, e a função que compara os elementos da lista e retorna o maior.

# In[15]:



print("""MENU:
         (0) Sair
         (1) Criar fração
         (2) Simplificar fração
         (3) Somar
         (4) Subtrair
         (5) Multiplicar
         (6) Dividir
         (7) Gerar lista de n frações
         (8) Somar lista
         (9) Maior fração""")


def sair():
    print("That's all folks :)))")
    
def criarFracao():
    numerador = int(input("Insira o numerador: "))
    denominador = int(input("Insira o denominador: "))
    return (numerador, denominador)

def verFracao(f):
    print(str(f[0])+"/"+str(f[1]))
    
def mdc(a,b):
    if a < b:
        return mdc(b, a)
    elif a%b == 0:
        return b
    else: 
        return mdc(a, a%b)

def simplificarFracao(f):
    num, denom = f
    a = mdc(num, denom)
    return (num/a, denom/a)    

def somarFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2 + n2*d1, d1*d2

def subtrairFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2 - n2*d1, d1*d2

def multiplicarFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*n2, d1*d2

def dividirFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2, d1*n2

def gerarLista():
    lista = []
    listaDecimal = []
    n = int(input("Insira o comprimento da lista: "))
    i = 0
    while i < n:
        num = int(input("Insira o numerador: "))
        den = int(input("Insira o denominador: "))
        tuplo = (num, den)
        lista.append(tuplo)
        listaDecimal.append(num/den)
        i += 1
    return lista

def somarLista(L):
    res = (0,1)
    for elem in L:
        f1 = res
        f2 = elem
        n1, d1 = f1
        n2, d2 = f2
        res = n1*d2 + n2*d1, d1*d2
    return res

def maiorLista(L):
    maior = -1000000000000000000000000
    listaDecimal = []
    i = -1
    for elem in L:
        elem = elem[0]/elem[1]
        listaDecimal.append(elem)
    for elem in listaDecimal:
        if elem > maior:
            maior=elem
            i+=1
    print("A maior fração é", L[i])
    return maior


def opcao():
    op = str(input("Insira um dos comandos do menu: "))
    while op != '0':
        if op == '1':
            f = criarFracao()
        elif op == '2':
            print(verFracao(simplificarFracao(f)))
        elif op == '3':
            f = somarFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '4':
            f = subtrairFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '5':
            f = multiplicarFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '6':
            f = dividirFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '7':
            lista = gerarLista()
        elif op == '8':
            f = somarLista(lista)
            print(verFracao(simplificarFracao(f)))
        elif op == '9':
            f = maiorLista(lista)
            print(f)
        else:
            print("Este número não está nas alternativas, tente novamente :D.\n")
        op = str(input("Insira um dos comandos do menu: "))
    if op == '0':
        sair()
opcao()

# In[ ]:




