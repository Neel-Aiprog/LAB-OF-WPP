#here we need to sort the heights of the CODEDEC team members the default height of team members is 1,2,3,4 and we need to give
#the output as the minimum number of swaps required
n=int(input())
l=[]
for i in range(0,4):
    a=int(input())
    l.append(a)
l1=sorted(l)
swap=0
for i in range(0,4):
    if(l[i]!=l1[i]):
        swap+=1
swap=int(swap/2)
print(swap)