class Node:
    def __init__(self,item=None,next_node=None):
        self.item = item
        self.next = next_node

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head is None
    
    def search(self,data):
        current = self.head
        while(current != None):
            if(current.item == data):
                return current
            current = current.next
        return None

    
    #adding a node at the starting of the linked list
    def addFirst(self,data):
        newNode = Node(data)
        if (self.is_empty()):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertInside(self,current,data):
        newNode = Node(data)
       
        if current == None:
            print("The given node cant't found")
        else:                       
            newNode.next = current.next
            current.next = newNode

    def addLast(self,data):
        newNode = Node(data)
        if(self.is_empty()):
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = newNode
            
    def deleteFirst(self):
        if(self.is_empty()):
            print("List is empty")
        elif(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next

    def deleteLast(self):
        if(self.is_empty()):
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = None

    def deleteInsideList(self,data):
        if(self.is_empty()):
            print("List is empty")
        elif self.head.item == data :
            self.deleteFirst()
        else:
            current = self.head
            while(current.next != None):
                if(current.next.item == data):
                    current.next = current.next.next
                    return
                current = current.next



     
  
   
    def display(self):
        current = self.head
        while(current):
            print(current.item,end=" ")
            current = current.next


list = LinkedList()
list.addFirst(3)
list.addFirst(1)
list.insertInside(list.search(1),2)
list.insertInside(list.search(3),4)
list.addLast(5)
print("Linked list before deleting is ",end=" ")
list.display()
print()
list.deleteInsideList(3)
print("Linked List after deleting ",end=" ")
list.display()

 