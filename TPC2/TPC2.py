#!/usr/bin/env python
# coding: utf-8

# # TPC2

# # Jogo "Adivinha o número em que pensei"

# ### (de 0 a 100)

# ### data de início: 2021-10-13

# ### data de fim: 2021-10-17

# ### supervisor: José Carlos Ramalho

# ### autor: Filipa Pinho Serra Campos, a95303

# O __TPC2__ consistiu em fazer o computador encontrar o número em que um utilizador pensa entre 0 e 100, com um __limite de 7 tentativas__. Para isto, o computador deveria propor ao utilizador um número e este deveria responder se o número pensado é maior ou menor do que o proposto até ser adivinhado o número.
# A estratégia pensada foi fazer o computador encontrar o número médio entre dois extremos e propor esse mesmo número. Os extremos iniciais foram o 0 e o 100. Após cada número proposto os extremos são alterados conforme a resposta do utilizador. Se o utilizador responde que o número escolhido é __maior__, é alterado o __extremo inferior__, sendo assim atribuído a esse o número proposto + 1. Por outro lado, se o número for __menor__, é alterado o __extremo superior__, atribuindo-lhe o valor do número proposto - 1.
# Cada vez que é proposto um número, o computador questiona ao utilizador se foi esse o número escolhido, ao que este deve responder "sim" ou "não". Ao receber uma resposta "sim" o computador dá o número como encontrado e o programa termina. Ao receber uma resposta "não", o computador recorre à estratégia do parágrafo anterior para propor um novo número.

# In[11]:


def adivinhar():
    encontrado = False
    minimo = 0
    maximo = 100
    meio = int((maximo + minimo) / 2)
    contador = 0
    
    print("o seu numero é :", meio, "?")
    acertou = str(input())
    
    while encontrado == False or minimo > maximo:
        if (acertou == "sim"):
            contador += 1
            print ("o contador acertou com ", contador, "tentativas")
            encontrado = True
            
        elif acertou == "nao":
            print("O número é maior ou menor? ")
            cimabaixo = str(input())
            
            if cimabaixo == "menor":
                maximo = meio - 1
                meio = int((maximo + minimo) / 2)
                print("o seu numero é :", meio, "?")
                acertou = str(input())
                
            elif cimabaixo == "maior":
                minimo = meio + 1
                meio = int((maximo + minimo) / 2)
                print("o seu numero é :", meio, "?")
                acertou = str(input())
               
            else:
                print("ERRO!!!!")
                contador -= 1
                
        else:
            print("ERRO!!!! O seu número é", meio, "?")
            acertou = str(input())
        contador += 1
    
adivinhar()
    


# In[ ]:




