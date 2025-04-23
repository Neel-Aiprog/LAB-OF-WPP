class bank():
    cus_acc=[123123,123345,3123124324,234324,1,2,3,4]
    print("WELCOME TO BANK PLS ENTER YOUR ACCOUNT NO:")
    acc=int(input())
    bal=0
    if(acc in cus_acc):
        print("ACCOUNT FOUND")
    else:
        print("Failure")
        exit()
    while(1>0):
        cho=int(input("choose deposital or withdrawal enter 1 or 0\t"))
        if(cho==-1):
            print("EXITING RN....")
            exit()
        if(cho==1):
            dep=int(input("enter your amount to deposit\t"))
            bal=bal+dep
        if(cho==0):
            wit=int(input("enter amount to be withdrawn\t"))
            if(wit>bal):
                print("low balance")
                exit()
            bal=bal-wit
            print(f"current balance:{bal}")
        else:
            print("wrong choice")
c=bank()
    