class bankacount():
    cus_acc=[123123,123345,3123124324,234324,1,2,3,4]
    print("WELCOME TO BANK PLS ENTER YOUR ACCOUNT NO:")
    acc=int(input())
    name=input("enter your name\t")
    bal=0
    def bank(self):
        if(self.acc in self.cus_acc):
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
                self.bal=self.bal+dep
            else:
                wit=int(input("enter amount to be withdrawn\t"))
                if(wit>self.bal):
                    print("low balance")
                    exit()
                self.bal=self.bal-wit
                print(f"current balance:{self.bal}")
    def details(self):
        print(f"Account no:{self.acc}")
        print(f"balance:{self.bal}")
        print(f"name:{self.name}")
c=bankacount()
c.bank()
c.details()
    