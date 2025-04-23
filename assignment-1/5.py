name=[]
for i in range(1,11):
    n=(input("enter your names\t"))#maximum char limit is 15
    if(len(n)>15):
        print("Maximum limit reached")
    name.append(n)

for i in range(0,10):
    name[i]=name[i][-1:-(len(name[i])+1):-1]
print(name)