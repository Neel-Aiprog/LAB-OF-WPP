n=int(input("enter how many points you want to convert\t"))
import numpy as np
c=np.ones((n,2))
for i in range(n):
    a=int(input())
    b=int(input())
for i in range(n-1):
    c[i][0]=a
    c[i][1]=b        
print("your normal coordinates::\t\n")
print(c)
print("\n")
for i  in range(n):
    l=c[i][0]
    m=c[i][1]
    r=np.hypot(l,m)
    t=np.arctan2(m,l)
    c[i][0]=r
    c[i][1]=t
print("here are your polar coordinates::\t\n")
print(c)
