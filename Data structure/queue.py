#FIFO
#first in first out

#use list to implement queue
#deque class
#collections module
#module is a collection of reusable codes

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#we use popleft() remove from left

queue.popleft()
print(queue)

if not queue:
    print("Empty!")