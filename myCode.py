#Code of singly Linked List
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #function to check if a linked list is empty or not
    def is_empty(self):
        return self.head is None
    
    #function to check if a node is present in linked list or not 
    def search(self,data):
        current = self.head
        while current:
            if current.item == data:
                return current
            current = current.next
        return None    
   
    
    #function to insert a node at the starting of singly linked list
    def insertAtHead(self,data):
        newNode = Node(data)
        if self.is_empty():            
            self.tail = newNode
        else:
            newNode.next = self.head
        self.head = newNode
        self.count += 1

    #function to insert a node at the end of singly linked list
    def insertAtTail(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode            
        else:
            self.tail.next = newNode
            newNode.next = None
        self.tail = newNode
        self.count += 1

    #function to insert a node after a particular node current
    def insertInside(self,current,data):
        if current is None:
            raise ValueError("Node is not Found in the Singly Linked List.")
        else:            
            if current == self.tail:
                self.insertAtTail(data)
            else:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                self.count += 1        
    
    #function to delete a node at the starting of Singly linked list
    def deleteAtFirst(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1

    #function to delete a node at the last of singly linked list
    def deleteAtLast(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current           
        self.count -= 1

    #function to delete a node inside a singly linked list
    def deleteInside(self,data):
        if self.is_empty():
            raise ValueError("Linked List is empty")
            return
        elif self.head.item == data:
            self.deleteAtFirst()
        elif self.tail.item == data:
            self.deleteAtLast()
        else:
            current = self.head
            while current.next is not None:
                if current.next.item == data:
                    current.next = current.next.next
                    break
                current = current.next
            self.count -= 1



    #function to print the Singly Linked List
    def display(self):
        current = self.head
        print("Singly Linked List is : ",end=" ")
        while(current):
            print(current.item,end=" ")
            current = current.next
        print()
    

list = SLL()
print(list.is_empty())
print("Size of Singly Linked List is ",list.count)
list.insertAtHead(5)

print("Size of Singly Linked List is ",list.count)
list.display()
print("Head of Singly Linked List ",list.head.item)
print("Tail of Singly Linked List ",list.tail.item)
list.insertAtHead(4)
list.insertAtHead(3)
list.insertAtHead(2)
list.insertAtHead(1)
list.insertInside(list.search(5),6)
print("Size of Singly Linked List is ",list.count)
list.display()
print("Head of Singly Linked List ",list.head.item)
print("Tail of Singly Linked List ",list.tail.item)
print(list.tail.next)
list.deleteInside(6)
print("Size of Singly Linked List is ",list.count)
list.display()
print("Head of Singly Linked List ",list.head.item)
print("Tail of Singly Linked List ",list.tail.item)
print(list.tail.next)
