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

    def findMid(self):
        slow = self.head
        fast = self.head

        while(fast != None  and   fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        return slow


list = SLL()
print(list.is_empty())
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.display()
print("Size of Singly Linked List is ",list.count)
mid = list.findMid()   
print(mid.item) 