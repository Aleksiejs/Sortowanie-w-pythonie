# coding: utf-8
#generowanie listy
import random

#funkcja generujaca liste losowych liczb w zasiegu od do
def generuj_liste(od,do):
    tab = []
    while od <= do:
        tab.append(od)
        od +=1
    random.shuffle(tab)
    return tab

lista = generuj_liste(1,10)
print(lista)

#sortowanie bąbelkowe
def babelkowe(lista):
    y = 0
    while y < (len(lista)+1):
        for x in range(len(lista)-1):
            if lista[x] > lista[x+1]:
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
        y +=1              
    return lista


#sprawdzenie czy działa
babelkowe(lista)

#sortowanie przez wstawianie
def wstawianie(lista):
    for i in range(len(lista)):
        klucz = lista[i]
        j = i-1
        while j>=0 and lista[j] > klucz:
            lista[j+1] = lista[j]
            j = j-1
        lista[j+1] = klucz
        
    return lista
        
#sprawdzenie czy działa
wstawianie(lista)

