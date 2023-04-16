class Node:
    def __init__(self, value):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()
        self.size = 0
    
    def __str__(self) -> str:
        current = self.LinkedList.head
        out = ""
        while(current):
            out += str(current.value) + "->"
            current = current.next
        return "Stack : " + out[:-2]
    
    def isEmpty(self):
        if(self.size == 0): 
            return "Stack is empty"

    def getSize(self):
        return self.size
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.LinkedList.head
        self.LinkedList.head = remove.next
        self.size -= 1
        return remove.value
    
    def peak(self):
        if self.isEmpty():
            raise Exception("Peakin from an empty stack")
        return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head = None
        
customStack = Stack()
print(customStack.isEmpty())

print("-"*10)
customStack.push(10)
customStack.push("Hello")
customStack.push(400)
customStack.push("Python")
print(customStack)

print("-"*10)
customStack.pop()
print(customStack)

print("-"*10)
print(customStack.peak())

print("-"*10)
print(customStack.delete())