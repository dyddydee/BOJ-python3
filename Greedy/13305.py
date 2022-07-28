import sys

'''n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))   # 2 3 1
cost = list(map(int, sys.stdin.readline().split())) # 5 2 4 1
sum = dis[0]*cost[0]
for i in range(len(dis)-1): # i 0 1 2
    min = cost[0]
    if cost[i]<cost[i+1]:
        sum += cost[i]*dis[i+1]
    else:
        min = cost[i+1]
        sum += min*dis[i+1]

print(sum)'''

n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))   
cost = list(map(int, sys.stdin.readline().split()))

sum = 0
m = cost[0]
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    sum += m * dis[i]

print(sum)


