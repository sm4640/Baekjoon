# 토마토
from collections import deque

m, n, h = map(int, input().split())


boxes = []
visited = [[[0]*m for _ in range(n)] for __ in range(h)]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
days = 0
done = False
for i in range(h):
    box = []
    for i in range(n):
        box.append(list(map(int, input().split())))
    boxes.append(box)

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == -1:
                visited[i][j][k] = 1
            elif boxes[i][j][k] == 1:
                visited[i][j][k] = 1
                q.append((days,i,j,k))

if sum(visited[i][j].count(0) for j in range(n) for i in range(h)) == len(q):
    done = True
    print(days)


if not done:
    while q:
        now, nh, nn, nm = q.popleft()
        if now != days:
            days += 1
        for i in range(6):
            if nh+dz[i] < 0 or nh+dz[i] > h-1 or nn+dy[i] < 0 or nn+dy[i] > n-1 or nm+dx[i] < 0 or nm+dx[i] > m-1 or visited[nh+dz[i]][nn+dy[i]][nm+dx[i]] == 1:
                continue
            boxes[nh+dz[i]][nn+dy[i]][nm+dx[i]] = 1
            visited[nh+dz[i]][nn+dy[i]][nm+dx[i]] = 1
            q.append((now+1, nh+dz[i], nn+dy[i], nm+dx[i]))

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 0:
                    days = -1

    print(days)