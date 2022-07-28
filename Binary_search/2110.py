import sys

n, c = map(int, sys.stdin.readline().split())
house = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    house.append(temp)

house.sort()
low = 1
high = max(house) #house[-1]

while low <= high:
    mid = (low + high) // 2
    cnt = 1 #공유기의 개수 카운트
    wifi = house[0]
    for i in range(1,n): # 1 2 4 8 9
        if house[i]-wifi >= mid:
            cnt += 1
            wifi = house[i]
    if cnt >= c:
        low = mid + 1
    else:
        high = mid - 1

print(high)
