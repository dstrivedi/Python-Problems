class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
class Queue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()
        
    def __str__(self) -> str:
        curr = self.linkedList.head
        out = ""
        while(curr):
            out += str(curr) + " -> "
            curr = curr.next
        return out[:-4]
    
    def enqueue(self, item):
        node = Node(item)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        tempNode = self.linkedList.head
        if self.isEmpty():
            return "Queue is empty."
        elif(self.linkedList.head == self.linkedList.tail):
            self.linkedList.head = None
            self.linkedList.tail = None
            return str(tempNode) + " deleted successfully from the front of the queue."
        else:
            self.linkedList.head = self.linkedList.head.next            
            return str(tempNode) + " deleted successfully from the front of the queue."
        
    def peak(self):
        if self.isEmpty():
            return "Queue is empty."
        else:
            return self.linkedList.head
        
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
            
customQueue = Queue()

customQueue.enqueue(10)
customQueue.enqueue([10,20,30])
customQueue.enqueue("Hello python")
customQueue.enqueue(True)
print(customQueue)

print("-"*10)
print(customQueue.peak())

print("-"*10)

print(customQueue.dequeue())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)

print("-"*10)
print(customQueue.peak())

print("-"*10)
print(customQueue.delete())



        
        