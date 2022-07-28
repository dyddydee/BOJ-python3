import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    target = [0 for i in range(n)]
    target[m] = 1

    while True:
        if num[0] == max(num):
            cnt += 1

            if target[0] != 1:
                del num[0]
                del target[0]
            else:
                print(cnt)
                break
        else:
            num.append(num.pop(0))
            target.append(target.pop(0))
            

