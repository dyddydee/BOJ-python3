import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

if sum(num) >= 0:
    total = sum(num)
    answer = total / n
    answer = answer + 0.5
    print(int(answer))
elif sum(num) < 0:
    total = sum(num)
    answer = total / n
    answer = answer - 0.5
    print(int(answer))

num.sort()
print(num[n//2]) 

count = Counter(num).most_common()
if len(count) == 1:
    print(count[0][0])
elif count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

ran = max(num) - min(num)
print(ran) 


