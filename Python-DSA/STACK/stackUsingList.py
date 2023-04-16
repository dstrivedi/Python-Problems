class Stack:
    def __init__(self, size) -> None:
        self.items = []
        self.top = 0
        self.size = size

    def push(self,item):
        # if(self.top > self.size):
        #     print("Stack is full")
        # else:
            self.items.append(item)
            self.top += 1
        
    def pop(self):
        if(self.top <= 0):
            print("Stack is empty")
        else:
            item = self.items.pop()
            self.top -= 1
            print(item)
    
    def peak(self):
        if(self.top <= 0):
            print("Stack is empty")
        else:
            print(self.items[-1])
    
    def size(self):
        print(self.top)
    
    def __str__(self):
        return str(self.items)
        
    
s = Stack(5)
print(s)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Initial stack:")
print(s)

s.push(6) #stack is full
print(s)

s.pop()
s.pop()
s.pop()
print(s)
s.peak()
s.pop()
s.pop()
s.pop()
s.peak()