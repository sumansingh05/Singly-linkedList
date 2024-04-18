class CollectionFramework:
    def __init__(self):
        self.ll = []

    def addFirst(self,data):
        self.ll.insert(0,data)

    def addLast(self,data):
        self.ll.append(data)

    def removeFirst(self):
        if len(self.ll) > 0:
            del self.ll[0]

    def removeLast(self):
        if len(self.ll) > 0:
            self.ll.pop()
        
    def __str__(self):
        return str(self.ll)    
       

ll = CollectionFramework()
ll.addFirst(1)
ll.addLast(2)
ll.addLast(3)
ll.addLast(4)
print(ll)

ll.removeLast()
print(ll)
ll.removeFirst()
print(ll)

    

    