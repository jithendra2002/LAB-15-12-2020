print("Jithendra Naidu-121910313053")
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,value):
        if self.head is None:
            new_node  = Node(value)
            self.head=new_node
        else:
            new_node = Node(value)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node    

    def search(self,value):
        temp=self.head
        while temp:
            if temp.data==value:
                return True
            temp=temp.next
        return False     
        
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

d=LinkedList()
N=int(input("enter the number of nodes u want to add to the linkedlist: "))
for i in range(N):
    d.append(input(f'Enter the node data'))
d.printList()     
a=input("Enter the value to check ")
print(d.search(a))
   
