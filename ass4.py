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
    
    def append(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def display(self):
        current = self.head
        print("Singly Linked List is :",end=" ")
        while(current):
            print(current.item,end=" ")
            current = current.next
        print()


list = SLL()
print(list.is_empty())
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.display()
print("Size of Singly Linked List is ",list.count)
    