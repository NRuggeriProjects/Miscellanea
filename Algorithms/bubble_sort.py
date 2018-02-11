''' List sorting algorithms '''


# first define the two types of bubble sort, to be called in the main function bubble_sort

def bbsort_classic(lis, in_place=False):
    ''' Classic Bubble Sort algorithm '''
    
    if in_place not in [True, False]:
        raise ValueError('in_place mst be either True or False')
        
    if in_place and len(lis)>1:
        
        flag=True
        while flag:
            flag=False
            for i in range(len(lis)-1):
                if lis[i]>lis[i+1]:
                    lis[i],lis[i+1]=lis[i+1],lis[i]
                    flag=True
    elif not in_place:
        l=lis.copy()
        if len(l)<=1:
            return l
        
        flag=True
        while flag:
            flag=False
            for i in range(len(l)-1):
                if l[i]>l[i+1]:
                    l[i],l[i+1]=l[i+1],l[i]
                    flag=True    
        return l
    

def bbsort_optimized(lis, in_place=False):
    ''' Bubble Sort with optimization: keeps track of the last swap position '''
    
    if in_place not in [True, False]:
        raise ValueError('in_place mst be either True or False')
        
    if in_place and len(lis)>1:      
        pos=len(lis)-1
        flag=True
        while flag:
            flag=False
            for i in range(pos):
                if lis[i]>lis[i+1]:
                    lis[i],lis[i+1]=lis[i+1],lis[i]
                    flag=True
                    pos=i   

    elif not in_place:
        l=lis.copy()
        if len(l)<=1:
            return l
        
        pos=len(l)-1
        flag=True
        while flag:
            flag=False
            for i in range(pos):
                if l[i]>l[i+1]:
                    l[i],l[i+1]=l[i+1],l[i]
                    flag=True
                    pos=i   
        return l
               
def shaker_sort(lis, in_place=False):
    ''' Shaker sort algorithm, variation of bubble sort  '''
    
    if in_place not in [True, False]:
        raise ValueError('in_place mst be either True or False')
        
    if in_place and len(lis)>1:
        pos=len(lis)-1
        flag=True
        while flag:
            flag=False
            for i in range(pos):                    # classic bubble sort  
                if lis[i]>lis[i+1]:
                    lis[i],lis[i+1]=lis[i+1],lis[i]
                    flag=True
                    pos=i   
            if flag==True:                    
                flag=False
                for i in range(pos,0,-1):           # reversed bubble sort
                    if lis[i]>lis[i+1]:
                        lis[i],lis[i+1]=lis[i+1],lis[i]
                        flag=True 
    elif not in_place:
        l=lis.copy()
        if len(l)<=1:
            return l
        
        pos=len(l)-1
        flag=True
        while flag:
            flag=False
            for i in range(pos):                
                if l[i]>l[i+1]:
                    l[i],l[i+1]=l[i+1],l[i]
                    flag=True
                    pos=i   
            if flag==True:                     
                flag=False
                for i in range(pos,0,-1):
                    if l[i]>l[i+1]:
                        l[i],l[i+1]=l[i+1],l[i]
                        flag=True                
        return l
    
    
 
# now define the main function calling all the others    

def bubble_sort(l=[], method='classic', in_place=False):
    '''
    Bubble Sort algorithm to sort lists.
        Inputs:
            -l, a list of numbers of objects with order value
            
            -method, the method called among 'classic','optimized','shaker'
            
            -in_place, to be True or False, defines if the algorithm modifies
                       the given list or returns a new ordered one
    '''
    
    if method not in ['classic','optimized','shaker']:
        raise ValueError('Method has to be either "classic", "optimized" or "shaker"')
        
    if in_place not in [True, False]:
        raise ValueError('in_place has to be either True of False')    
    
    if method=='classic':
        return bbsort_classic(l,in_place)
    elif method=='optimized':
        return bbsort_optimized(l,in_place)
    else:
        return shaker_sort(l,in_place)
                

                


            
                
                
                
                
                
                
                
                
     








           
