# 연결 요소의 개수

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0] * (n+1)

g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

count = 0

for i in range(1, len(g)):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        k = q.popleft()
        for j in range(len(g[k])):
            if not visited[g[k][j]]:
                q.append(g[k][j])
                visited[g[k][j]] = 1
    count += 1

print(count)

