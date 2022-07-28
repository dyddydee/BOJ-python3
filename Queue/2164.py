import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(range(1,n+1))


'''queue.popleft()
queue.append(queue.popleft())

print(queue)
print(len(queue))'''

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())