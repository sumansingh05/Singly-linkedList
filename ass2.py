class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    #add a new node at the starting of the linked list
    def insertAtFirst(self,data):
        newNode = Node(data)
        if(self.is_empty()):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    

    #add a new node at the end
    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            temp = self.head
            while (temp.next != None) :
                temp = temp.next
            temp.next = newNode

    #deleting first node in singly linked list
    def deleteFirst(self):
        if(self.is_empty()):
            print("List is empty!")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next

    def deleteInsideList(self,data):
        if(self.is_empty()):
            print("List is empty")
        elif self.head.data == data:
            self.deleteFirst(data)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            



    def deleteLast(self,data):
        if (self.is_empty()):
            print("The list is empty.")
        elif self.head.next == None:
            self.head == None
        else:
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = None


    def display(self):
        temp = self.head
        while (temp):
            print(temp.item,end=" ")
            temp = temp.next

list = LinkedList()
list.insertAtFirst(10)
list.insertAtEnd(11)
# list.insertAtEnd(25)
#list.insertAtEnd(56)
print("List before deleting")
#list.insertAtEnd(99)
list.display()
print()
list.deleteFirst()
print("List after deleting")
list.display()



