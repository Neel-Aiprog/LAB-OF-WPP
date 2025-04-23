# input rhinoceros
# output rHiNoCeRoS
string_1=input("enter your string\t")
for i in range(0,len(string_1)):
    if(i%2==0):
        print(string_1[i],end="")
    if(i%2!=0):
        print(string_1[i].upper(),end="")