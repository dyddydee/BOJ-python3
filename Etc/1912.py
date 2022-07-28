import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [0] * len(num)
dp[0] = num[0]

for i in range(1, len(num)):
    dp[i] = max(num[i], dp[i-1]+num[i])

print(max(dp))