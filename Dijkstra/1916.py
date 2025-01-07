# 최소비용 구하기

import sys, heapq

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append((b,c))

s, d = map(int, input().split())

cost = [float('inf') for _ in range(n+1)]
q = []
heapq.heappush(q, (0,s))
cost[s] = 0
while q:
    dist, now = heapq.heappop(q)

    if cost[now] < dist:
        continue

    for i in g[now]:
        if dist + i[1] < cost[i[0]]:
            cost[i[0]] = dist + i[1]
            heapq.heappush(q, (cost[i[0]], i[0]))

print(cost[d])