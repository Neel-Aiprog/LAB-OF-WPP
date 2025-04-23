import numpy as np
r=int(input("enter number of rows\t"))
c=int(input("enter number of columns\t"))
a=np.ones((r,c),dtype=object)
for i in range(0,r):
    for j in range(0,c):
        d=int(input())
        a[i][j]=d
for i in range(0,r):
    for j in range(0,c):
        a[i][j]=f"_______{a[i][j]}_______"
        
print(a)