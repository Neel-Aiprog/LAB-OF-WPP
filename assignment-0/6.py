num1=int(input("pls enter the number you want to reverse\t"))
sum=0
sumd=0
num2=num1
while(num2!=0):
    q=int(num2%10)
    sumd+=1 #here sumd is used to reverse the number and to count the place of digits so as when we will reverse it we can multiply it in powers of  10
    num2=int(num2/10)
while(num1!=0):
    q=int(num1%10)
    sumd-=1
    sum=sum+q*(10**sumd) #here we are adding the respective numbers with powers of 10 into the sum
    num1=int(num1/10) #here int typecasting is required so that operation is performed successfully and we dont get num1 as float type
print(sum)