import random
l=[]
l1=[]
zeroc=0
for i in range(1,101):
    num=random.randint(0,1)
    l.append(num)

for i in l:
    if(i==0):
        zeroc+=1
    if(i==1):
        l1.append(zeroc)
        zeroc=0
print(l)
print(l1)
print(max(l1))
