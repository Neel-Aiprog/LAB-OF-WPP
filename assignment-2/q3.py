test=int(input("enter number of test cases\t"))
case=[]
dcount=0
for i in range(0,test):
    num=int(input())
    case.append(num)

for i in case:
    dcount=0
    while(i!=0):
        q=i%10
        if(q!=0):
            if(i%q==0):
                dcount+=1
        i=int(i/10)
    print(dcount)
    