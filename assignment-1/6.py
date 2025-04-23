import math
#lets consider a 3d space and we are going to input 3 points
x=[]
y=[]
z=[]
for i in range(1,11):
    a=int(input("enter your x coordinate \t"))
    x.append(a)
    b=int(input("enter your y coordinate \t"))
    y.append(b)
    c=int(input("enter your z coordinate \t"))
    z.append(c)
coord=list(zip(x,y,z))
near=[]
for i in coord:
    min=float('inf')
    for j in coord:
        if(i==j):
            continue
        distance=math.sqrt(pow(j[0]-i[0],2)+pow(j[1]-i[1],2)+pow(j[2]-i[2],2))
        if(distance<min):
            min=distance
            near1=j
    near.append(near1)  
print(near)       