class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    #search a node is present in the linked list or not
    def search(self,data):
        current = self.head
        while(current):
            if(current.data == data):
                return current
            current = current.next
        return None
    
    #add a node at the starting of the linked list
    def addFirst(self,data):
        newNode = Node(data)
        if(self.is_empty()):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.count += 1

    #add a node at the last of the linked list
    def addLast(self,data):
        newNode = Node(data)
        if(self.is_empty()):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode 
            self.tail = newNode
        self.count += 1

    #add a node inside the linked list after a given node
    def insertAfter(self,current,data):
        if current is None:
            raise IndexError("Node is not found in the Linked List")        
        else:
            if(current is self.tail):
               self.addLast(data)
               return
            else:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode           
                self.count += 1

    #delete a node at the starting of singly linked list
    def deleteFirst(self):
        if self.is_empty():
            raise IndexError("Linked List is empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1

    #delete a node at the last of singly linked list
    def deleteLast(self):
        if self.is_empty():
            raise IndexError("Linked List is empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while(current.next != self.tail):
                current = current.next

            current.next = None
            self.tail = current
        self.count -= 1

    #deleting a node inside the singly linked list
    def deleteInside(self,data):
        if self.is_empty():
            raise IndexError("Linked List is empty")
        else:
            if self.head.data == data:
                self.deleteFirst()
                return
            elif self.tail.data == data:
                self.deleteLast()
                return
            else:
                current = self.head
                while(current.next):
                    if(current.next.data == data):
                        current.next = current.next.next
                        self.count -= 1
                        break
                    current = current.next

    #function to display the singly linked list
    def display(self):
        if self.is_empty():
            raise IndexError("Linked List is empty")
        current = self.head
        print("Singly Linked List is",end=" ")
        while(current):
            print(current.data,end=" ")
            current = current.next
        print()

ll = SLL()
ll.addFirst(1)
ll.addLast(2)
ll.addLast(3)
ll.insertAfter(ll.search(3),4)
ll.display()
print("Head of Singly Linked List is ",ll.head.data)
print("Tail of Singly Linked List is ",ll.tail.data)
print("Size of Singly Linked List is ",ll.count)
ll.deleteInside(4)
ll.display()
print("Head of Singly Linked List is ",ll.head.data)
print("Tail of Singly Linked List is ",ll.tail.data)
print("Size of Singly Linked List is ",ll.count)