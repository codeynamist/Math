import random
from matplotlib import pyplot as plt
ry=100000
pts=[1,2,3]
xx=300
j,k=0,0
p,q,r=0,xx/2,xx
x,y,z=0,xx,0
a,b=[p,q,r],[x,y,z]
plt.plot(a,b,'bo')
while ry>0:
    ro=random.choice(pts)
    x1=a[ro-1]
    y1=b[ro-1]
    x2=j
    y2=k
    j=(x1+x2)/2
    k=(y1+y2)/2
    ry-=1
    m=[x1,x2]
    n=[y1,y2]
    plt.plot(m,n,'go',markersize=0.1)    
