"""
double ended queue
O(1)
"""

from collections import deque
queue = deque()

queue.append("Ravi")
queue.append("Priya")
queue.append("You")
queue.append("Karan")

print(queue)

first = queue.popleft()
print(first)
print(queue)

print(queue[0])
print(len(queue))
print(len(queue)==0)