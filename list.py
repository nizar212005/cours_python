import numpy as np
import matplotlib.pyplot as plt

"""
L = [3, "a",2.5,True]

L.append(6) # <==> .insert(len(L),6)
L.insert(0,40)
"""
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



"""
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],[15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
plt.show()
"""

x = x_axe()
y = syracuse(nombre)


fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()




















