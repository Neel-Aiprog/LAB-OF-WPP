class queue():
    def create(self):
        self.items=[]
    def enqueue(self,data):
            self.items.append(data)
    def dequeue(self):
        if(not(self.items)):
            print("empty! ")
            exit() 
        x=self.items.pop(0)
        return x
    def display(self):
        print(self.items)
q=queue()
choice=0
q.create()
print("you have successfully created queue\t\n")
while(1>0):
    choice=int(input("\nenter your choice\t\n"))
    match(choice):
        case 0:
            print("exiting rn!!!")
            exit()
        case 1:
            print("\nyou have chosen enqueue operation\t\n")
            data=int(input("enter data you want to enqueue\t"))
            q.enqueue(data)
        case 2:
            print("\nyou have chosen dequeue operation\t\n")
            q.dequeue()
        case 3:
            print("\nyou have chosen to display your queue\t\n")
            q.display()
        case _:
            print("wrong choice try again!")