import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    num.append(temp)

num.sort()

for i in range(n-1):
    num[i+1] += num[i]

num.pop(0)
print(num)
    