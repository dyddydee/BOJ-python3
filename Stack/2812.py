import sys

n, k = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline())

answer = []
cnt = k

for num in number:
    while answer and cnt>0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))