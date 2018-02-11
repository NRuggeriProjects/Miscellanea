import random
from math import sqrt
import matplotlib.pyplot as plt

def weighted_choice(weights):
    ''' Chooses an element with probabilty given by its weight 
        on a total of weights. Uses the "roulette method". Info at 
        http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python'''
        
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i
        
        
def d(p1,p2):
    ''' Euclidean distance between two points in R^n '''
    
    return sqrt(sum( 
                [(p1[i]-p2[i])**2 for i in range(len(p1))]   
                ))
    
    
def KPlusPlus_iterate(l,m):
    ''' Given a list of points and the means already found, makes a steps of
        the k++ method '''
        
    weights= [ min([d(x1,x2) for x2 in m ]) **2 if x1 not in m else 0
                 for x1 in l ]
    return l[weighted_choice(weights) ]
    

def KPlusPlus(l,k):
    ''' Implements the k++ algorithm on a list l, to be passed afterwards to
        the k-means. Returns the set of the k mean points selected '''
    
    means=[]          # list of means selected
    means.append(l[random.randint(0,len(l)-1)])
    for i in range(k-1):
        means.append(KPlusPlus_iterate(l,means))
    return means

def KMeans_iterate(l,m):
    ''' Iterates one step of the k-means algorithm, returning the new clusters '''
    
    k=len(m)
    clusters=[[] for i in range(k)]
    for p in l:
        dist=[d(p,mean) for mean in m ]
        i=dist.index(min(dist))
        clusters[i].append(p)
    return clusters

def centroid(cluster):
    return tuple([
                    sum([p[i] for p in cluster])/len(cluster) 
                        for i in range(len(cluster[0]))
                ])
    
def KMeans(l,m):
    ''' Implements the k-means algorithm with the means m on the list l '''
    
    m_old=[]
    m_new=m
    while m_new!=m_old:
        m_old=m_new
        clusters=KMeans_iterate(l,m_old)
        m_new=[centroid(c) for c in clusters]
    return clusters,m_new
    

def randpoint(x=1,y=1):
    ''' Returns a random point with cohordinates in 
        [0,x),[0,y) '''
    try:
        return (random.random()*x,random.random()*y)
    except ValueError:
        print("Insert complex,real or integer number as cohordinates ")


# now try the algorithm with random points
x,y=1,1
points=[]
for i in range(1000):
    points.append(randpoint(x,y))
 
x_cohord=[p[0] for p in points]
y_cohord=[p[1] for p in points]
plt.plot(x_cohord,y_cohord,'ro')
plt.title('Random points in [0,%d)x[0,%d)'%(x,y))
plt.show()

k=5
m=KPlusPlus(points,k)
clusters, means=KMeans(points,m)
for i in range(k):
    x=[p[0] for p in clusters[i]]
    y=[p[1] for p in clusters[i]]
    mean=means[i]
    plt.plot(x,y,'.',mean[0],mean[1],'bo')
plt.show()
for i in range(k):              # plots with connected lines, to visualize differently
    x=[p[0] for p in clusters[i]]
    y=[p[1] for p in clusters[i]]
    mean=means[i]
    plt.plot(x,y,mean[0],mean[1],'bo')
plt.show()
    

    
    
    
    
    
    
    
    
    
