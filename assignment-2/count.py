count=[1,2,3,4,1,1]
search=int(input())
count1=0
for i in count:
    if i==search:
        count1+=1
print(count1)
t=(1,2,3,4,5)
count=0
search1=int(input())
for search in t:
    count+=1
print(count)
string="abcdabcd"
string1=input()
index=0
for i in range(0,len(string)-len(string1)+1):
    if(string[i:i+len(string1)]==string1):
            index+=1
print(index)
