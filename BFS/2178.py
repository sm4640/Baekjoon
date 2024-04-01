# 미로탐색
from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(input())

check = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0,0))
check[0][0] = 1

while q:
    a, b = q.popleft()
    for i in range(4):
        na = a + dy[i]
        nb = b + dx[i]
        if na < 0 or na > n-1 or nb < 0 or nb > m-1:
            continue
        if maze[na][nb] == '1' and check[na][nb] == 0:
            q.append((na,nb))
            check[na][nb] = check[a][b] + 1

print(check[n-1][m-1])
