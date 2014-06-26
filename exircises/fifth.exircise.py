# coding=utf-8
__author__ = 'WiktorMarchewka'
import math
import cmath
def quadratic(a,b,c):
    #obliczanie delty
    delta=b**2-4*a*c
    #warunek ktory zaklada ze delta jest mniejsza od zera, obliczanie x1 i x2
    if delta <0:
        x1=(-b+cmath.sqrt(delta))/2*a
        x2=(-b-cmath.sqrt(delta))/2*a
        return x1,x2
    #co jesli delta jest wieksza badz rowna 0    
    else:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        return x1,x2
#Przykłady
print(quadratic(1,0,9))

print(quadratic(1,0,4))
