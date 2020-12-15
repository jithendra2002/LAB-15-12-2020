print("Jithendra Naidu-121910313053")
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


    def printList(self):
        temp=self.head
        while(temp):
            print(temp.value)
            temp=temp.next
list1=LinkedList()
list1.head=Node(10)
second=Node(20)
third=Node(30)
list1.head.next=second
second.next=third
list1.printList()

        
