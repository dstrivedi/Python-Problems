from collections import deque

#declaring deque
dq = deque([1,2,3,4,5])
print("deque : ", dq)

# using append() to insert element at right end
# inserts 4 at the end of deque
dq.append(6)

#to insert element at left end
dq.appendleft(0)

print("deque after append and appendleft : ",dq)

#to delete element from right end
dq.pop()

#to delete element from left end
dq.popleft()

print("deque after pop and popleft : ",dq)

