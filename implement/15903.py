# 카드 합체 놀이

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
total = sum(cards)

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    new = x + y
    heapq.heappush(cards, new)
    heapq.heappush(cards, new)
    total = total - x - y + (new*2)

print(total)


