# 유기농 배추

import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t):
    count = 0
    m,n,k = map(int, input().split())
    visited = [[1]*m for _ in range(n)]
    cab = []
    for j in range(k):
        x, y = map(int, input().split())
        visited[y][x] = 0
        cab.append((y,x))

    for j, l in cab:
        if visited[j][l]:
            continue
        q = deque()
        count += 1
        q.append((j,l))
        while q:
            a, b = q.popleft()
            visited[a][b] = 1
            for h in range(4):
                na, nb = a+dy[h], b+dx[h]
                if na > n-1 or nb > m-1 or na < 0 or nb < 0:
                    continue
                if visited[na][nb]:
                    continue
                q.append((na, nb))
                visited[na][nb] = 1
    print(count)