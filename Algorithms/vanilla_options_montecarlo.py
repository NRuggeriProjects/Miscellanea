''' Pricing european call options (discrete case) with Monte-Carlo method  '''

import random

def weighted_choice(weights):
    ''' Chooses an element with probabilty given by its weight 
        on a total of weights. Uses the "roulette method". Info at 
        http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python'''
        
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i
        

def price(N=3,M=1,p=0.5,u=2,d=0.5,iter=1000):
    ''' Pricing an european call option with parameters as above:
        -N is the number of periods
        -u,d are the values with which the underlying asset evolves: 
            it can assume value X_(n+1)= u*X_n or d*X_n
        -p is the probability of u occurring at every step
        -M is given by the pricing formula: max(X_N-M , 0)
        Assuming interest rate r=0   '''
    
    if p>1 or p<0:
        raise ValueError("The probability p has to be in [0,1]")
        
    sum=0
    for i in range(iter):
        u_occur=[weighted_choice([p,1-p]) for n in range(N) ].count(0)
        X_N=u**u_occur+ d**(N-u_occur)
        sum+=max( X_N-M , 0 )
        
    return sum/iter
        
    
    
    
    
    
    
    
    
    
    