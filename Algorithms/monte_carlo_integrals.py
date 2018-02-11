''' Monte-Carlo integrals calculation '''

import random
import scipy.optimize as optimize 

        
def randpoint(x_min=0,x_max=1,y_min=0,y_max=1):
    ''' Returns a random point with cohordinates in 
        [x_min,x_max),[y_min,y_max) '''
    try:
        return  (
                random.random()*(x_max-x_min)+x_min,
                random.random()*(y_max-y_min)+y_min
                )
    except ValueError:
        print("Insert complex,real or integer number as cohordinates ")
        

def function_range(f,a,b):
    ''' Returns the sup and inf of the function f in [a,b] '''
    
    inf= optimize.minimize_scalar(f, 
                                  method='bounded',
                                  bounds=(a,b)
                                  ).fun
    sup= -1*optimize.minimize_scalar(lambda x: -1*f(x),
                                     method='bounded',
                                     bounds=(a,b)
                                     ).fun
    
    return inf,sup


def random_integrate(f,a,b,n=1000):
    ''' Integrates the function f in the range [a,b). 
        f has to be a single variable function. 
        n is the number of random points used  '''

    if a>b:
        raise ValueError("a must be lesser or equal than b")
    elif a==b:
        return 0
    
    inf,sup= function_range(f,a,b)
    
    count=0
    for i in range(n):
        p=randpoint(a,b,inf,sup)
        if f(p[0])>p[1] and p[1]>0:
            count+=1
        elif f(p[0])<p[1] and p[1]<0:
            count-=1
    
    return (b-a)*(sup-inf)*count/n
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


