def main(string):
    string=list(string)
    n=len(string)
    count=0
    if(string.count(string[0])==n):
        return"no answer"        
    i=n-2
    while(i>=0 and string[i]>=string[i+1]):
        i-=1
    if(i==-1):
        return "".join((string))
    j=n-1
    while(j>=0 and string[j]<=string[i]):
        j-=1
    string[j],string[i]=string[i],string[j]
    string[i+1:]=reversed(string[i+1:])
    return"".join(string)

test=int(input("enter the number of test cases\t"))
ans=[]
for i in range(0,test):
    string1=input()
    ans.append(main(string1))
for i in ans:
    print(i)    
                