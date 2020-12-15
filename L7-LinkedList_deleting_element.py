class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        
    def inputs(self,value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next!= None:
                temp = temp.next
            temp.next = new_node

    def deleting_node(self,value):
        temp=self.head
        if temp is not None:
            if temp.data==value:
                temp.next=None
                return
        while temp is not None:
            if temp.data==value:
                break
                prev = temp
                temp = temp.next
            else:
                return
        prev.next = temp.next
        temp=None
        
    def display_LinkedList(self):
         temp = self.head
         while temp:
             print(temp.data)
             temp = temp.next


list1=LinkedList()
n=int(input("Enter number of nodes you want add to linkedlist"))
for i in range(n):
    list1.inputs(input(f'Enter the {i}th node value'))
d=input("Enter the key u want to remove from the linked list")
list1.deleting_node(d)
list1. display_LinkedList()
                
            
            
        
