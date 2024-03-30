#code of singly Linked list

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None


    def is_empty(self):
        return self.head is None
    
    #insert a node at the starting of the singly linked list
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
    #insert a node at the end of the singly linked list
    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def search(self,data):
        current = self.head
        while(current!=None):
            if(current.item == data):
                return current
            current = current.next
        return None
    
    #insert a node after a particular index  in the singly linked list
    def insert_after(self,current,data):
        if  current == None:   #if the node is not found
            print("The given node cannot be found")
            return
        else:
            if current == self.tail:
                self.insertAtEnd(data)
            else:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode

    #prints the elements present inside the Linked List
    def display(self):
        current = self.head
        print("Singly Linked List is: ",end=" ")
        while(current):
            print(current.item,end=' ')
            current = current.next

    #deleting a node at the starting of the linked list
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.head=self.head.next

    #deleting a node at the end of the linked list
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
               current = current.next 
            current.next = None
            self.tail = current

     #delete  a node in between the nodes of the singly linked List 
    def deleteInside(self,data):
        if  self.is_empty():
            print("List is empty")        
        else:
            if self.head.item == data:
                self.delete_first()
            elif self.tail.item == data:
                self.delete_last()
            else:
                current = self.head
                while(current.next != None):
                    if(current.next.item == data):
                        current.next = current.next.next
                        return
                    current = current.next
                         
             
             

list = SLL()            
list.insertAtStart(5)
list.insertAtStart(1)
list.insertAtEnd(10)
list.insertAtEnd(11)
list.insert_after(list.search(5),6)
list.display()
print()
print("Head of Singly linked List ",list.head.item)
print("Tail of Singly linked List ",list.tail.item)
print()
list.deleteInside(11)
list.display()
print()
print("Head of Singly linked List ",list.head.item)
print("Tail of Singly linked List ",list.tail.item)


