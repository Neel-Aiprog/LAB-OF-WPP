def digital_root(num):
    sum=0
    while(num>0):
        q=num%10
        sum+=q
        num=int(num/10)

    print(sum)
def main():
    n=int(input("enter the number you want digital root of\t"))
    digital_root(n)
if(__name__=="__main__"):
    main()