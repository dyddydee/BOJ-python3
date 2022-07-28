#정수를 저장하는 큐를 구현한 다음. 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오. 

import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([]) #데크(deque) : 양방향 큐로 앞,뒤 양쪽에서 element를 추가하거나 제거할 수 있음. 

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
