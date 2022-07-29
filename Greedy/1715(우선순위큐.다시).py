import sys
import heapq

n = int(sys.stdin.readline())
card = list(int(sys.stdin.readline()) for _ in range(n))
heapq.heapify(card)
answer = 0

while len(card) != 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    sum = first + second
    answer += sum
    heapq.heappush(card, sum)

print(answer)
    