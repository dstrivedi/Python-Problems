#initialise queue list
queue = []

#enqueue in list
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print(queue)

#dequeue from list in FIFO/LILO manner
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)
