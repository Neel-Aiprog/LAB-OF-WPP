pro={}
n=int(input("enter how many products do you want to enter\t"))
for i in range(0,n):
    name=input("enter name\t")
    price=input("enter price\t")
    pro.update({name:price})
for j in pro:
    n=input(" enter name\t")
    if(n in pro):
        print(f"price:{pro[n]}")
    if(n=='-1'):
        exit()
    if(not(n in pro)):
        print("your item is not found")