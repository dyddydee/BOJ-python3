import sys
n,m = map(int, sys.stdin.readline().split())
sum_of = list(map(int, sys.stdin.readline().split())) #누적 합 배열 선언
# 5 4 3 2 1 -> 0 5 9 12 14 15
for i in range(n-1):
    sum_of[i+1] += sum_of[i] # 5 9 12 14 15
sum_of = [0] + sum_of

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_of[b]-sum_of[a-1])
