#code of singly Linked list

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode

    def search(self,data):
        current = self.head
        while(current!=None):
            if(current.item == data):
                return current
            current = current.next
        return None
    
    def insert_after(self,current,data):
        if  current==None:   #if the node is not found
            print("The given node cannot be found")
            return
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode

    def display(self):
        current = self.head
        while(current):
            print(current.item,end=' ')
            current = current.next


    def delete_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.head=self.head.next

    def delete_last(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while(current.next.next != None) :
                current = current.next
            current.next = None

        
    def deleteInside(self,data):
        if  self.is_empty():
            print("List is empty")
        elif self.head.item == data:
            self.delete_first()
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
list.deleteInside(11)
list.display()


