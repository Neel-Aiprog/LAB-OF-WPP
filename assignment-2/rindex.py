string="abcdabcd"
string1=input()
index=0
ind=[]
for i in range(len(string)-len(string1),-1,-1):
    if(string[i:i+len(string1)]==string1):
            index=i
            break
if(index==-1):
    print("Value error")
else:
    print(index)