from re import X
import sys

n = int(sys.stdin.readline()) # 6
a = list(map(int, sys.stdin.readline().split())) #10 20 10 30 20 50

memorization = [0]

for x in a:
    if memorization[-1] < x:
        memorization.append(x)
    else: #memorization의 맨 끝 원소보다 x가 작거나 같은 경우.
        low = 0
        high = len(memorization)
        while low <= high:
            mid = (low + high) // 2
            if memorization[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        memorization[high] = x

print(len(memorization) - 1)
print(memorization, end=' ')


