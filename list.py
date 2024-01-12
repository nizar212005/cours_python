import numpy as np
import matplotlib.pyplot as plt
from random import random, shuffle
"""
L = [3, "a",2.5,True]

L.append(6) # <==> .insert(len(L),6)  #dir help(list)
L.insert(0,40)
def f(l):
    l.append(4)

--------------references(globales et locales)------------------------------------------------------------------------
l =[1,2,3]
f(l)
print(l)


L = [1,2,3]
T = L
L[0]=5
print(T)


R=[5,8,7]
L.extend(R)

l.sort() /l.sort(reverse=True)
------------------fonction_count--------------------------------------------------------------------
def compte(L,e):
    compte = 0
    for i in L:
        if i == e:
            compte += 1
    return compte

---------------------------------syracuse_algorithm-------------------------------------------------------------
def prochain_term(n):
    if n%2==0:
        return n//2
    return 3*n+1
def syracuse(n):
    if n == 1 :
        L=[1]
        return L
    L = [n]
    i = prochain_term(n)
    while i > 1:
        L.append(i)
        i = prochain_term(i)
        
    L.append(1)
    return L

nombre = 10
def longeur_syracuse(n):
    list = [0]
    for i in range(1,n+1):
        list.append(len(syracuse(i)))
    return list


# print(syracuse(nombre))
# print(longeur_syracuse(100))


def x_axe():
    m = []
    for i in range (len(syracuse(nombre))):
        m.append(i)
    return m 




# fig, ax = plt.subplots()
# ax.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],[15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
# plt.show()


x = x_axe()
y = syracuse(nombre)

fig, ax = plt.subplots()
ax.plot(x,y)
# plt.show()    
-----------------------------------------------------------------------------------------------------------

s = [int(x) for x in input().split()]

-----------------------------------------------------------------------------------------------------------------------
def inverser(L):
    T = []
    for i in L:
        T.insert(0,i)
    return T
print(inverser(L))
"""



def maxi(L):
    if L == []:
        return None
    m = L[0]
    for i in L:
        if i>m:
            m = i
    return m
# print(maxi(L))




    
def sort_(L):  #tri par selection
    T=[]
    for i in range(len(L)):
        T.append(max(L))
        L.remove(max(L))   
    return T

# print(sort_(L))
L = [5,3,7,8,2,6]

def trie(L): #tri par insertion
    T = [L[0]]
    for i in range(1,len(L)):
        f = False
        for j in range(len(T)):
            if L[i]<T[j]:
                T.insert(j,L[i])
                f = True
                break
        if f == False:
            T.append(L[i])
    return T
    
                
    return T


print(trie(L))
        
        
def tri_a_bulles(L):

    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j]>L[j+1]:
                c = L[j]
                L[j]=L[j+1]
                L[j+1]=c
    return L

#print(tri_a_bulles(L))

def est_trie(L):
    
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
        return True
     
T = [5,3,7,2,6]
print(est_trie(T))

def tri_stupide(L):
    
    while not est_trie(L):
        shuffle(L)
    return L

# print(tri_stupide(T))


def fusion(T,L1,L2):
    i,j,k = 0 
    while i<len(L2) and j < len(L1):
        if L2[i]<L1[j]:
            T[k]=L2[i]
            i+=1
        else:
            T[k]=L1[j]
            j+=1
        k+=1
    return T
def tri_fusion(L):
    m = len(L)//2
    l1 = L[:m+1]
    l2 = L[m+1:]

    tri_fusion(l1)
    tri_fusion(l2)
    fusion(L,l1,l2)

print(tri_fusion(L))


















