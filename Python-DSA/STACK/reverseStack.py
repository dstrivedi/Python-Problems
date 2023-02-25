class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def display(self):
        for data in self.items:
            print(data)
            
def insert_at_bottom(s,item):
    if s.is_empty():
        s.push(item)
    else:
        popped = s.pop()
        insert_at_bottom(s,item)
        s.push(popped)
            
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s,popped)
            
s = Stack()
data_list = input("Please enter the elements to stack : ").split()
for data in data_list:
    s.push(int(data))
print("The Stack:")
s.display()

reverse_stack(s)
print("After reversing : ")
s.display()
