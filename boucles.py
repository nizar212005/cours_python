"""

mcpc

---------equivalence--------------------------------

for k in range(i,j,p):
    instruction
    <==>
k = i
while k<j :
    instruction
    k += p

---------------break au nb pair---------------------------

n = int(input("entrer un nombre"))
n = 1
while n%2 != 0 :
    n = int(input("entrer un nombre"))
    print(n)

print("fin")

----------DIVISION EUCLIDIENNE-----------------------

a = int(input("entrer un nombre "))
b = int(input("entrer un nombre "))

r,q = a,0

while b <= r :
    r -= b
    q =q+1 
print("r=",r,"et q=",q)

-----Combien de fois doit-on la plier au minimum pour que l'épaisseur dépasse la hauteur de la tour Eiffel 324 m.---------------------------
e = 0.1
p = 0

while e <= 324000:
    e *= 2
    p+=1
print(p)
-----------somme_des_chiffrs_d'un_nbr-------------------------------------------------

n = int(input("entrer un nombre : "))
s = 0

while n != 0:
    c = n % 10
    s += c 
    n = n//10
print(s)


-----------------inverser_les_chiffres_d'un_nbr-------------------------------

nombre = int(input("entrer un nombre "))

n_copie = nombre

n_inverse = 0
while n_copie > 0:
    c = n_copie % 10 #dernier chiffre
    n_inverse = (n_inverse*10) + c # ajouter ce chiffre a la fin du nb inverse
    n_copie //= 10 # supprimer le dernier chiffre de la copie du nombre originale
print(n_inverse)

------------------triangle_cenre-----------------------------

n = int(input("entrer un nombre :"))
for i in range (1, n+1):
     print(" "*(n-i)+"*"*(2*i-1))

-------------(2)----------------------
n = int(input("entrer un nombre : "))
for i in range (0,n+1):
    print((n-i)*'#'+" "+i*"#")

----------littlegame-----------------------
n=int(input("entrez un nombre:"))
for i in range(1,n+1):
    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:   
        print(i)




#--------------somme_triangulaire--------------------
n = int(input("entrer un nbr "))
s = 0
#s_int = 0
for i in range(0,n+1):
    s_int = 0
    for j in range(0,i+1):
        s_int += j**2
        print(i,j)
    s += s_int
print(s)


---------------approximation_de_e----------------------------------
n=int(input("entrez un nombre de preference tres grand: "))
s=0
for i in range(0,n+1):
    p=1
    for j in range(1,i+1):
        p=p*(1/j)
    s=s+p
print(s)


"""


n = int(input("entrer un nombre : "))













