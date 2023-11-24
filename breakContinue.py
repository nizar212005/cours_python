
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
print("fin")
break continue


#################nombre_premier##################################################"

n = int(input())
flag = False
if n == 1:
    print(f"{n}n'est pas premier")
elif n > 1:
    for i in range(2,n):
        if n % i == 0:
           flag = True
           break
    #print(flag)
    if flag:
        print(f"{n}n'est pas premier")
    else: print(f"{n} est premier")


#############somme des diviseurs d'un nombre###########################################""
n = int(input())
d = 0

for i in range(1,n+1):
    if n % i == 0:
        d += i

print(d) # on peut tester si cest un nombre parfait (6 = 1+2+3 / 28 = 1+2+4+7+14)

------------------------------------------------------------------
  for n in range(6,10000):
    d = 0

    for i in range(1,n+1):
        if n % i == 0:
            d += i
            
    

    if n == d :
        print(n,"c'est nombre parfait")
print("fin")


     
            
"""



s = "kjhjhd"
print(len(s))

















            
    