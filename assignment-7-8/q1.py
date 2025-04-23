class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def display(self):
        if(self.head is None):
            print("your linked list is empty")
        temp=self.head
        while (temp!=None):
            print(f"{temp.data}\t",end="")
            temp=temp.next
    def insert_at_begin(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
            return
        new.data=data
        new.next=self.head
        self.head=new
    def insert_at_end(self,data):
        if(self.head==None):
            self.head=newe
            return
        newe=node(data) 
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newe
    def delete(self):
        if(self.head is None):
            self.head=None
            return
        temp=self.head
        while(temp.next.next is not None):
            temp=temp.next
        temp.next=None
ll = linkedlist()
ll.insert_at_begin(1)
ll.display()
print("\n")
ll.insert_at_begin(2)
ll.display()
print("\n")
ll.insert_at_begin(3)
ll.display()
print("\n")
ll.insert_at_end(0)
ll.display()
print("\n")
ll.delete()
ll.display()
print("\n")
ll.delete()
ll.display()
print("\n")  