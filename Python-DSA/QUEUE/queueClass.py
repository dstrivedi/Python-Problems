class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.top = 0
        self.last = 0
        
    def push(self,item):
        if(self.top >= self.size):
            print("Queue is full")
        else:
            self.queue.append(item)
            self.top += 1
    
    def pop(self):
        if(self.top <= 0):
            print("Queue is empty")
        else:
            item = self.queue.pop(self.last)
            self.top -= 1
            print(item)
        
    def front(self):
        if(self.top <= 0):
            print("Queue is empty")
        else:
            print(self.queue[-1])

    def rear(self):
        if(self.top <= 0):
            print("Queue is empty")
        else:
            print(self.queue[0])
    
    def __str__(self):
        return str(self.queue)
    
q = Queue(5)

q.push(1)
q.push(3)
q.push(5)
q.push(7)
q.push(9)

print("Initial Queue : ",q)

q.pop()

print("After dequeue : ",q)

q.front()
q.rear()



    