import sys

n = int(sys.stdin.readline())

line = []
for i in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort()
line.insert(0,[0,0])

dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))