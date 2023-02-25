stack = [];

print("Initial stack")
stack.append(10); #index 0
stack.append(20);
stack.append(30);
stack.append(40);
stack.append(50);

print("Stack : " , stack);

print(stack.pop()) #remove last element in LIFO order
print(stack.pop())

print("Stack after pop operation : ", stack);
    
    