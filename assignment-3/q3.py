#the original height of utopian tree is 1m and at the end of monsoon cycle it height doubles while at the end of the second cycle its height increases by 1m
def utopian(n):
    height=1
    for i in range(1,n+1):
        if(i%2!=0):
            height=height*2
        else:
            height+=1
    print(f"height at the end of  cycle no. {n} is {height}")
def main():
    test=[]
    t=int(input("enter number of testcases\t"))
    for i in range(0,t):
        te=int(input())
        test.append(te)
    for i in test:
        utopian(i)
if(__name__=="__main__"):
    main()