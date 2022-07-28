import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(tree)


while low <= high:
    mid = (low + high) // 2
    res = 0 #자른 나무의 총 합 저장
    for i in tree:
        if i >= mid:
            res += i - mid
    if res >= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)