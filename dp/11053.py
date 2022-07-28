import sys

n = int(sys.stdin.readline())
dp = [0] * 1001
answer = 0
num = list(map(int, sys.stdin.readline().split()))
num.insert(0,0) # 0 10 20 10 30 20 50 

for i in range(1, n+1):
    for j in range(0, i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)
    #answer = max(answer, dp[i])


#print(answer)
#print(dp)  #0 1 2 1 3 2 4
print(max(dp))