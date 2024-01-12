import numpy as np
import matplotlib.pyplot as plt
 


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def suite(n):
    if n == 0:
        return 3
    return 2*suite(n-1)

# print(suite(3))

def fibo(n):
    if n == 0 or n == 1 :
        return 1
    return fibo(n-1) + fibo(n-2)

# def fib():
#     L = []
#     for i in range(10):
#         L.append(fibo(i))
#     return L
# def x():
#     T = []
#     for i in range(len(fib())):
#         T.append(i)
#     return T

# fig,ax =plt.subplots()
# ax.plot(x(),fib())
# plt.show()



def C(k,n):
    if k == 0 or k == n:
        return 1
    return C(k,n-1) +C(k-1,n-1)

# def comb(n):
#     L=[]
#     for i in range(n):
#         L.append(C(i,n))
#     return L
# def x(k,n):
#     T = []
#     for i in range(len(comb(n))):
#         T.append(i)
#     return T
        


# fig,ax =plt.subplots()
# ax.plot(x(5,10),comb(10))
# plt.show()




L = [5,8,3,1,2]
def f_max(L):
    if len(L)==1:
        return L[0]
    m1 = L[0]
    print(m1)
    m2= f_max(L[1:])
    
    
    if m1>m2:
        return m1
    return m2
print(f_max(L))

def somme(L):
    if len(L) == 1:
        return L[0]
    return L[0] + somme(L[1:])

def f(a,b):#multiplicatuion
    if b == 1:
        return a
    return a + f(a,b-1)
# ackermann

def fleche(a,b,n): # a$n => a^n  , a$$n => a^(a^(a......^(a))) n fois 
    if n == 1:
        return a**b
    x = a
    for i in range(b-1):
        x = fleche(a,x,n-1)
    return x

print(fleche(2,3,2))



def recherche(L,e):
    # if e in L:
    #     return True
    # return False
    for i in L:
        if i == e:
            return True
    return False
str()
def rechereche_dicho(L,e):
    print(f'on cherche {e} dans L')
    if len(L)==0:
        return False
    m = len(L)//2
    if  L[m]==e:
        return True
    elif e < L[m]:
        
        return rechereche_dicho(L[:m],e)
    return rechereche_dicho(L[m+1:],e)

T = [2,5,6,8,10]
print(rechereche_dicho(T,10))









    