def fibo(n):
    a=0
    b=1
    c=1
    while(c<n): 
        c=a+b
        if(n==c):
            print("IsFibo")
        a=b
        b=c
    if(c>n):
        print("IsNotFibo")
def main():
    nums=[]    
    t=int(input("enter number of testcases\t"))
    for i in range(0,t):
        num=int(input())
        nums.append(num)
    for i in nums:
        fibo(i)
if(__name__=="__main__"):
    main()