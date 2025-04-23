def main():  
    l=int(input("enter your left side limit\t"))
    r=int(input("enter your right side limit\t"))
    maxxor=[]
    for i in range(l,r+1):
        for j in range(l,r+1):
            maxxor.append(i^j)
    print(max(maxxor))   
if(__name__=="__main__"):
    main()