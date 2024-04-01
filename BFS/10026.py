# 적록 색약
from collections import deque

n = int(input())

area = []
area1 = []
check = [[0]*n for _ in range(n)]
check1 = [[0]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
count1 = 0

for i in range(n):
    area.append(input())

for i in range(n):
    area1.append(area[i].replace('G', 'R'))

def bfs(area, check, count):
    for i in range(n):
        for j in range(n):
            if check[i][j] != 0:
                continue
            count += 1
            c = area[i][j]
            q = deque()
            q.append((i,j))
            check[i][j] = count
            while q:
                a, b = q.popleft()
                for k in range(4):
                    na = a + dy[k]
                    nb = b + dx[k]
                    if na < 0 or na > n-1 or nb < 0 or nb > n-1:
                        continue
                    if area[na][nb] == c and check[na][nb] == 0:
                        q.append((na,nb))
                        check[na][nb] = count
    return count

print(bfs(area, check, count), bfs(area1, check1, count1))