# DFS 와 BFS
from collections import deque
import heapq

n, m, v = map(int, input().split())

node = [[] for _ in range(n+1)]
node1 = [[] for _ in range(n+1)]

check = [0] * (n+1)
check1 = [0] * (n+1)

bfs = []
dfs = []

for i in range(m):
    a, b = map(int, input().split())
    heapq.heappush(node[a], b)
    heapq.heappush(node[b], a)
    heapq.heappush(node1[a], (-b, b))
    heapq.heappush(node1[b], (-a, a))

q = deque()
q.append(v)
check[v] = 1
while q:
    a = q.popleft()
    bfs.append(a)
    while node[a]:
        b = heapq.heappop(node[a])
        if check[b] == 0:
            q.append(b)
            check[b] = 1

s = []
s.append(v)
while s:
    a = s.pop()
    if check1[a] == 1:
        continue
    check1[a] = 1
    if a not in dfs:
        dfs.append(a)
    while node1[a]:
        b = heapq.heappop(node1[a])[1]
        if check1[b] == 0:
            s.append(b)

print(*dfs)
print(*bfs)