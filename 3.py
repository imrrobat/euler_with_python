#Code By MrRobot
#Plz Subscribe!

from math import sqrt

l = []

def prim(n):
    while n%2==0:
        l.append(2)
        n = n/2
    
    for i in range(3,int(sqrt(n))+1,2):
        while n%i==0:
            l.append(i)
            n = n/i
    
    if n>2:
        l.append(int(n))

prim(600851475143)
print(l)
