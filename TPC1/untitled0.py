# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:32:33 2021

@author: pipap
"""
import random
from random import randrange

def firstjogador():
    print ("Pode começar a jogar!! :) ")
    total = 21
    
    while total > 0 :
        nfj = int(input("Quantos fósforos quer retirar? ")) 
        if nfj < 1 or nfj > 5 or total < nfj :
            print ("Não é possível retirar essa quantidade de fósforos!")
            return
        elif nfj == 5 :
            nfc = 5
            total -= nfj
        else:
            total -= nfj
            print ("Após a sua jogada sobraram ", total, " fósforos :) ")
            nfc = 5 - nfj
        total = total - nfc     
        if total > 0 :
            print ("Sobraram ", total ," fósforos após a jogada do computador :) ")
        else:
            print("Perdeu :( ")

def firstcomputador():
    print ("Vai jogar em segundo lugar :/ ")
    total = 21
    
    nfc = randrange(1, 6)
    print ("O computador retirou ", nfc, " fósforos :)")
    total -= nfc
    print ("Sobraram ", total, " fósforos :)")
    
    while total > 0:
        nfj = int(input("Quantos fósforos quer retirar? ")) 
        if nfj < 1 or nfj > 5 or total < nfj :
            print ("Não é possível retirar essa quantidade de fósforos!")
            return
        else :
            total -= nfj
            if total == 0:
                print ("Perdeu :(( ")
                return
            totaljogada = 21-total
            resJ = totaljogada % 5
            
            if resJ == 0 :
                nfc = randrange(1, 6)
            else : 
                nfc = 5 - resJ
            print ("O computador retirou ", nfc, " fósforos :)")
            total -= nfc
            if total <= 0:
                print ("GANHOUUU!!! PARABÉNS!!! :)")
                return
            print ("Sobraram ", total, " fósforos :)")
            
            
def jogar() :
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("x  Bem vindo ao jogo dos fósforos :)      x")
    print("x                                         x")
    print("x  Vai ser sorteado o primeiro jogador    x") 
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    primeirojogador = ['computador', 'utilizador']
    escolha = random.choice(primeirojogador)
    if escolha == 'computador' :
        firstcomputador()
    else :
        firstjogador()
jogar()