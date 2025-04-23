#we need to create a list that contains integers from 0 to 49
#we need to print a list in order 'a','bb','ccc','dddd','eeeee'........
a=[]
sq=[]
char=[]
j=97
for i in range(0,50):
    a.append(i)
for i in range(0,51):
    sq.append(i**2)
for i in range(1,27):
    char.append(i*chr(j))
    j+=1
print(char)