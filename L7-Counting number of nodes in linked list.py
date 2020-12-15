#linked list with user inputs
print("121910313053","JITHENDRA NAIDU ARNIPALLI")
class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self): 
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

       
   
    def getCount(self):
        temp = self.head  
        count = 0  

        
        while (temp):
            count += 1
            temp = temp.next
        return count
    def print_list(self):
        cur = self.head
        while cur:
           
            print(cur.data)
            cur = cur.next
ll = LinkedList()  
size = int(input("Enter the number of elements:"))

for i in range(size):
    k = input("Enter the data : ")
    ll.push(k)

print("The Linked List is : ")
ll.print_list()

print("The number of nodes in the list is:",ll.getCount())
