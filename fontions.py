
"""

def carre(x):  # \n => retour a la ligne 
    for i in range(x):
        print("hello world \t") 
carre(3)
              
carre(5)

def addition(x, y=10):  # le deuxieme argument est facultatif
    return x + y
print(addition(1))  
print(addition(1,2))

def func():
    return
print(func())

----------------------------------------------------------------
def pgcd(x,y):
    if x < y :
        return # pas la peine de faire else car return va arreter la fonc
    while y % x != 0:
        c = y
        y= x % y
        x = c
    return y
print(pgcd(13,2))

def foo(): # concept des varibles locales et globales
    a = 5
    print(a) # affiche 5
#print(a) erreur 'a' not defined 
a = 10
foo()
print(a) # affiche 10

"""



























