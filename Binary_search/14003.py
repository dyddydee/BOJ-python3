import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = []
cnt = [0]
for i in range(n):
    low = 0
    high = len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid] < num[i]:
            low = mid + 1
        else:
            high = mid - 1
    if low >= len(dp):
        dp.append(num[i])
        cnt.append(low)
    else:
        dp[low] = num[i]
        cnt.append(low)

print(len(dp))

max_cnt = max(cnt)
answer = []
max_idx = cnt.index(max_cnt)

while max_idx >= 0:
    if cnt[max_idx] == max_cnt:
        answer.append(num[max_idx-1])
        max_cnt -= 1
    max_idx -= 1

answer.reverse()
#del answer[0]
print(*answer)


