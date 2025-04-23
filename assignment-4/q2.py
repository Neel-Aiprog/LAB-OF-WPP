import math
case=int(input("enter the number of test cases\t"))
d=[]
a1=[]
b1=[]
count=0
for i in range(0,case):
    a=int(input())
    b=int(input())
    a1.append(a)
    b1.append(b)
d=list(zip(a1,b1))
for i,j in d:
    count=int(math.sqrt(j))-int(math.sqrt(i))
    print(count)