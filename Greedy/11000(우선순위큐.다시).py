import sys

n = int(sys.stdin.readline())
time = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    time.append(temp)

time.sort(key = lambda x: (x[1], x[0]))

last = time[0][1]
cnt = 0
print(last)
for x, y in time:
    if x < last:
        cnt += 1
    
print(cnt)
