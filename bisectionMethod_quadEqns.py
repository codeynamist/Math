import random as rd

ct,val,dp=[],[],[]
p=int(input("a: "))
q=int(input("b: "))
r=int(input("c: "))
D=q**2-4*p*r

def func(x):
    return p*x**2+q*x+r
    
def bisection(a,b):
    while (func(a) * func(b) >= 0):
        a=rd.randint(-100,100)
        b=rd.randint(-100,100)   
    while (abs(b-a) >= 0.0001):
        c = (a+b)/2
        if (func(c) == 0.000):
            break
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
    c=round(c,4)
    if round(c,2) not in dp:
        val.append(c)
        dp.append(round(c,2))
if D==0:
    print("The only root is:",-q/(2*p))
elif D<0:
    print('The roots are complex. Use a different Method of calculation. Bisection method works only for "Real Roots"')
else:
    while len(val)<2:
        a,b =0,0
        bisection(a,b)
    
for i in val:
    if i not in ct:
        ct.append(i)
for i in range(len(ct)):
    print("The root",i+1, "is:",ct[i])
