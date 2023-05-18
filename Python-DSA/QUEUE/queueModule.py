import multiprocessing
import queue as q
from multiprocessing import Queue

customQueue = q.Queue(maxsize=5)
multiprocessingQueue = Queue(maxsize=5)

print(customQueue.qsize())
print(multiprocessingQueue.qsize())

customQueue.put(1)
customQueue.put([1,2,4,5])
customQueue.put(["Hello"])
customQueue.put("Python")
customQueue.put(0)

multiprocessingQueue.put(1)
multiprocessingQueue.put([1,2,4,5])
multiprocessingQueue.put(["Hello"])
multiprocessingQueue.put("Python")
multiprocessingQueue.put(0)

print(customQueue.full())
# print(customQueue.get())
print(customQueue.qsize())
print(customQueue.empty())


print(multiprocessingQueue.full())
print(multiprocessingQueue.get())
print(multiprocessingQueue.qsize())
print(multiprocessingQueue.empty())