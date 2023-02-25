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
            
def palindrome(s):
    reversed_text = ""
    while not s.is_empty():
        reversed_text = reversed_text + s.pop()
    return reversed_text
    
            
s = Stack()
str = input("Enter string: ")
for chr in str:
    s.push(chr)
s.display()

reversed_text = palindrome(s)
if(str == reversed_text):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")
