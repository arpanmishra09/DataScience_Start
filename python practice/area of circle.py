import math as m

def area(r):
    p = m.pi * (r**2)
    return p

r = float(input('enter the radius of the circle'))

a= area(r)
print(a)