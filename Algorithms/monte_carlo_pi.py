''' Approximating Pi wih Monte-Carlo method  '''

from random import random
from math import *
import time
import matplotlib.pyplot as plt

def d(p1,p2):
    ''' Euclidean distance between two points in R^n '''
    
    return sqrt(sum( 
                [(p1[i]-p2[i])**2 for i in range(len(p1))]   
                ))
    
    
def randpoint(x=1,y=1):
    ''' Returns a random point with cohordinates in 
        [0,x),[0,y) '''
    try:
        return (random()*x,random()*y)
    except ValueError:
        print("Insert complex,real or integer number as cohordinates ")
        

def approx_pi(n):
    '''Approximates Pi using Monte-Carlo method with n points '''
    # Consider the circle centered in (1,1) with radius 1 and the circumscribed square
    
    c1=time.clock()
    points_in_circle=0
    for i in range(n):
        if d(randpoint(2,2),(1,1))<1: points_in_circle+=1
    c2=time.clock()
    
    return 4*points_in_circle/n,c2-c1

    
pi_values=[]
times=[]
print("Values found and calculation times:\n ")
for n in [1000,10000,100000,1000000]:
    r=approx_pi(n)
    pi_values.append(r[0])
    print(r)
    times.append(r[1])
    errors=[abs(value-pi) for value in pi_values]
    
    
# As one can see, the method is not very efficient
plt.plot([1000,10000,100000,1000000],errors)
plt.yscale('log')
plt.title("Logarithmic error against the number of sample points")
plt.show()

plt.plot([1000,10000,100000,1000000],times)
plt.title("Calculation time against the number of sample points")
plt.show()



    
    
    
    
    
    
    
    
    
    
    
