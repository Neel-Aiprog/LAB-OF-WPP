st=input()
if(len(st)%2==0):
    odd1=[]
    odd2=[]
    for i in range(0,int(len(st)/2)):
        odd1.append(st[i:i+1])
    for i in range(int(len(st)/2),len(st)):
        odd2.append(st[i:i+1])
    odd2.reverse()
    count=0
    for i in range(0,len(odd1)):
        count+=abs(ord(odd1[i])-ord(odd2[i]))#here if the value is negative it will convert it into positive
    print(count)    
else:
    odd1=[]
    odd2=[]
    for i in range(0,int(len(st)/2)):
        odd1.append(st[i:i+1])
    for i in range(int(len(st)/2)+1,len(st)):
        odd2.append(st[i:i+1])
    odd2.reverse()#reverse comparison will be easy
    count=0
    for i in range(0,len(odd1)):
        count+=abs(ord(odd1[i])-ord(odd2[i]))#here if the value is negative it will convert it into positive
    print(count)    