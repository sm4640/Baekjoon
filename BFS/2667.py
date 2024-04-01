# 단지번호 붙이기
from collections import deque

n = int(input())
dan = []

for i in range(n):
    dan.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
check = [[0]*n for _ in range(n)]

dan_num = 0

for i in range(n):
    for j in range(n):
        if dan[i][j] == '0' or check[i][j] != 0:
            continue
        else:
            dan_num += 1
            q = deque()
            q.append((i,j))
            check[i][j] = dan_num
            while q:
                a, b = q.popleft()
                for k in range(4):
                    na = a + dy[k]
                    nb = b + dx[k]
                    if na < 0 or na > n-1 or nb < 0 or nb > n-1:
                        continue
                    if dan[na][nb] == '1' and check[na][nb] == 0:
                        q.append((na,nb))
                        check[na][nb] = dan_num

print(dan_num)
totals = []
for num in range(1, dan_num+1):
    total = 0
    for c in check:
        total += c.count(num)
    totals.append(total)

totals.sort()
for total in totals:
    print(total)