def main():
    slice=[]
    mul=[]
    test=int(input("enter the number of test cases\t"))
    for i in range(1,test+1):
        k=int(input())
        slice.append(k)
    for i in range(0,len(slice)):
            mul=[]
            if(slice[i]==1):
                print("1")
                continue
            for j in range(1,slice[i]+1):
                for l in range(1,slice[i]+1):
                    if(j+l==slice[i]):
                        mul.append(l*j)
            print(max(mul))
if(__name__=="__main__"):
    main() 