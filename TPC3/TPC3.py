# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:54:45 2021

@author: pipap
"""
n=int(input("Introduza o número de elementos da lista:"))
l=[]
for j in range (n):
    elemento=int(input("introduza o elemento: "))
    l.append(elemento)
def bubble_sort(l):
    i = 0
    l1 = []
    for elem in l :
        l1.append(elem)
    print(l1)
    while i < (len(l) - 1):
        if l[i] > l[i + 1]:
            l.insert(i, l[i + 1])
            l.pop(i+2)
            i += 1
        else:
            i += 1
            
    print(l)
    print(l1)
    while l1 != l:
        i = 0
        l1 = []
        for elem in l :
            l1.append(elem)
        while i < (len(l) - 1):
            if l[i] > l[i + 1]:
                l.insert(i, l[i + 1])
                l.pop(i+2)
                i += 1
            else:
                i += 1
bubble_sort(l)
print(l)


