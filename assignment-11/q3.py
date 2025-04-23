import pandas as pd

data1=[]
n=int(input("enter no. of cars:"))
for car in range(n):
    item=int(input("enter asking price:"))
    data1.append(item)

data2=[]
for car in range(n):
    item=int(input("enter fair price:"))
    data2.append(item)
asking_price=pd.Series(data1)
fair_price=pd.Series(data2)
result=[]
for i in range(n):
    if(asking_price[i]<fair_price[i]):
        result.append(i)
print("following are the indices corresponding to good deals")
print(result)