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

    #function to reverse a singly Linked List
    def reverseList(self):
        current = self.head
        prev = None

        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.tail = self.head
        self.head = prev

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

    def findMid(self,head):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    #check if a linked list is palindrome or not
    def checkPalindrome(self):
        if self.head is None or self.head.next is None:
            return True
        
        #find mid
        midNode = self.findMid(self.head)

        #reverse second half
        prev = None
        current = midNode

        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next

        right = prev    #right half head
        left = self.head

        #check left half and right half
        while(right is not None):
            if(left.data is not right.data):
                return False
            left = left.next
            right = right.next

        return True
    

    #check if a cycle is found in linked list 
    def checkCycle(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head.next
        
        while(fast != None  and  fast.next != None):
            if(slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
            
            
        return False
    
    # implementing merge sort in linked list
    def merge(self,head1,head2):
        mergedLL = Node(-1)
        temp = mergedLL

        while head1 is not None  and  head2 is not None:
            if head1.data <= head2.data:
                temp.next = head1
                head1 = head1.next
                temp = temp.next
            else:
                temp.next = head2
                head2 = head2.next 
                temp = temp.next


        if head1 is not None:
            temp.next = head1
            
        elif head2 is not None:
            temp.next = head2

        # update temp to the last node of merged list
        while temp.next is not None:
            temp = temp.next
            
        return mergedLL.next   

      

    #implementing merge sort in the singly linked list
    def mergeSort(self,head):
        if head is None  or  head.next is None:
            return head
        
        # split the linked list into two halves
        prev = None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # recursively sort each half        
        left = self.mergeSort(head)
        right = self.mergeSort(slow)

        # it merge the sorted halves
        return self.merge(left,right)
         
        

ll = SLL()

ll.addFirst(1)
ll.addLast(2)
ll.addLast(3)
ll.insertAfter(ll.search(3),4)
ll.addLast(5)
ll.addLast(6)
ll.addLast(7)
ll.display()
print("Head of Singly Linked List is ",ll.head.data)
print("Tail of Singly Linked List is ",ll.tail.data)
print("Size of Singly Linked List is ",ll.count)
#ll.deleteInside(4)
ll.reverseList()

ll.display()
print("Head of Singly Linked List is ",ll.head.data)
print("Tail of Singly Linked List is ",ll.tail.data)
print("Size of Singly Linked List is ",ll.count)
print(ll.checkPalindrome())
print(ll.checkCycle())
# ll.head = ll.mergeSort(ll.head)
# ll.display()