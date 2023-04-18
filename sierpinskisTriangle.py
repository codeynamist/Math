#This code generates Sierpinski's triangle when given 4 inputs. 3 inputs in cartesian coordinates (p,x),(q,y),(r,z).
#Or if you want an equilateral triangle, you can just specify xx, which is the max value in x and y coordinates.
#Then 1 more inout is given (j,k), which is the initial guess point. 
#By default, the no. of iterations is taken as 100000, you can change it as you like.

#The concept behind the working of this code is that, 3 initial points are taken in a cartesian space and a 4th point is assumed in a random place.
#Now a random point out of the initial 3 points is taken and the mid point between the taken random point and chosen 4th point is the new 4th point. 
#Again a random point out of the 3 is taken and the mid point between 4th point and the randomly chosen new point is the new 4th point. 
#This process is repeated for all iterations and this will give a Sierpinski's triangle Fractal. 

#The beauty is that, even if you take random guess very far away from the initial triangle, the fractal triangle would still form. 
#The code generates the fractal even if the initial guess is in a region where the points should actually not lie.

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
