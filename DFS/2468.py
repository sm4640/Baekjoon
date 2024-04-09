# 안전 영역

n = int(input())

region = [list(map(int, input().split())) for _ in range(n)]

rain = 0
flood = [[0] * n for _ in range(n)]
flood_count = 0

answer = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while flood_count != n * n:
    rain += 1
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if flood[i][j] == 1:
                continue
            if region[i][j] <= rain:
                flood[i][j] = 1
                flood_count += 1
    
    count = 0
    for i in range(n):
        for j in range(n):
            if flood[i][j] == 0 and check[i][j] == 0:
                s = [(i,j)]
                while s:
                    a, b = s.pop()
                    if check[a][b] == 1:
                        continue
                    check[a][b] = 1
                    for k in range(4):
                        na = a + dy[k]
                        nb = b + dx[k]
                        if na in (-1, n) or nb in (-1, n):
                            continue
                        if flood[na][nb] == 0 and check[na][nb] == 0:
                            s.append((na,nb))
                count += 1
    if count > answer:
        answer = count

print(answer)