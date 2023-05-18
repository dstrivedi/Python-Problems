# using size limit
class CircularQueue:
    def __init__(self, maxSize) -> None:
        self.maxSize=maxSize
        self.list = maxSize*[None]
        self.front = -1
        self.rear = -1
    
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return " ".join(values)
    
    def isFull(self):
        if self.rear + 1 == self.maxSize and self.front == 0:
            return True
        elif self.rear + 1 == self.front:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.front == -1:
            return "Queue is empty."
        else:
            return "Queue is not empty."
    
    def enqueue(self, item):
        if self.isFull():
            return "Queue is full."
        else:
            if self.rear + 1 == self.maxSize:        
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
            self.list[self.rear] = item
            return str(item) + " is inserted at the end of Queue."
        
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty."
        else:
            firstElement = self.list[self.front]
            front = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front = 0
            else:
                self.front += 1
            self.list[front] = None
            return firstElement
    
    def peak(self):
        if self.front == -1:
            return "Queue is empty."
        else:
            return self.list[self.front]

    def delete(self):
        self.list = self.maxSize * [None]
        self.front = -1
        self.rear = -1    

circularQueue = CircularQueue(5)

print(circularQueue.isEmpty())

print("-"*10)
print(circularQueue.enqueue(10))
print(circularQueue.enqueue("Hello"))        
print(circularQueue.enqueue("Python"))
print(circularQueue.enqueue(1000))
print(circularQueue.enqueue(4000))
print(circularQueue)

print("-"*10)
print(circularQueue.enqueue("Queue"))

print("-"*10)
print(circularQueue.dequeue())
print(circularQueue)

print("-"*10)
print(circularQueue.peak())