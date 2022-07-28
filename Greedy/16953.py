import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1
while True:
    if a == b:
        break
    elif b%10 == 1: #b를 10으로 나눈 나머지가 1인경우 
        b = b//10
        cnt += 1
    elif b%2 == 0:
        b = b//2
        cnt += 1
    elif a > b:
        cnt = -1
        break
    else:
        cnt = -1
        break
    
print(cnt)

#예를 들어서 어떤 수 B를 계속 나누다가 53에서 멈췄는데 A보다는 클 경우 , 
# 반복문에서 탈출하지 못하고 갇히게 되어 시간초과가 발생된다는 것이다.