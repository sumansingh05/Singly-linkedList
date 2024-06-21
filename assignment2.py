#code of singly linked list

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
    

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def is_empty(self):
        return self.head is None
    
    #insert a node at the starting of singly linked list
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.count += 1

    #insert a node at the last of the singly linked list
    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    #search a node is present in the linked list or not
    def search(self,data):
        current = self.head
        while(current != None):
            if(current.item == data):
                return current
            current = current.next
        return None
    
    #print the linked list
    def display(self):
        current = self.head
        print("Singly Linked is:",end=" ")
        while(current):
            print(current.item,end=" ")
            current = current.next
        print()

list = SLL()
list.insertAtStart(3)
list.insertAtStart(2)
list.insertAtStart(1)
list.insertAtEnd(4)
list.insertAtEnd(5)
list.display()