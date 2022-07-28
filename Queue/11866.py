import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque(range(1,n+1))
answer = []
 
for i in range(n):
    queue.rotate((n-i)-k+1)
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")