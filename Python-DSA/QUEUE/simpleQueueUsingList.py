class Queue:
    def __init__(self) -> None:
        self.list = []
        self.size = 0
        
    def __str__(self) -> str:
        values = [x for x in self.list]
        return "".join(str(values))
    
    def isEmpty(self):
        if self.size == 0:
            return "Queue is empty."
        else:
            return "Queue is not empty."
    
    def enqueue(self, value):
        self.list.append(value)
        self.size += 1
        return str(value) + " inserted successfully in Queue."
    
    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        else:
            poppedItem = self.list.pop(0)
            self.size -= 1
            return str(poppedItem) + " deleted successfully from Queue."
    
    def peak(self):
        if(self.size == 0):
            raise Exception("Peaking from an empty Queue.")
        else:
            return "Top element in Queue is " + str(self.list[0])
    
    def delete(self):
        self.list = []
        self.size =0
        
customeQueue = Queue()

print(customeQueue.isEmpty())

print("-"*10)
print(customeQueue.enqueue(10))
print(customeQueue.enqueue("Hello"))
print(customeQueue.enqueue("Python"))
print(customeQueue.enqueue([1,2,3,4]))
print(customeQueue)

print("-"*10)
print(customeQueue.peak())

print("-"*10)
print(customeQueue.dequeue())
print(customeQueue)

