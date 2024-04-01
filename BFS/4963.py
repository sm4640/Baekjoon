# 섬의 개수
from collections import deque

w, h = map(int, input().split())

answer = []

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while w != 0 and h != 0:
    maps = [list(map(int, input().split())) for _ in range(h)]
    check = [[0]*w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 0 or check[i][j] != 0:
                continue
            count += 1
            q = deque()
            q.append((i,j))
            check[i][j] = 1
            while q:
                a, b = q.popleft()
                for k in range(8):
                    na = a + dy[k]
                    nb = b + dx[k]
                    if na < 0 or na > h-1 or nb < 0 or nb > w-1:
                        continue
                    if maps[na][nb] == 1 and check[na][nb] == 0:
                        q.append((na,nb))
                        check[na][nb] = 1
    answer.append(count)

    w, h = map(int, input().split())

for a in answer:
    print(a)