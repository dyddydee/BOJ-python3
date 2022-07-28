import sys

n = int(sys.stdin.readline())
stack = []
cur = 1 #현재 숫자의 값? 
answer = []
flag = 0
for i in range(n):
    num = int(sys.stdin.readline())
# 4 3 6 8 7 5 2 1 입력 받음 ..
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
