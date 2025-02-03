# 봄버맨

import sys

input = sys.stdin.readline

r, c, n = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

all_bomb = {(i,j) for i in range(r) for j in range(c)}
bomb = set()
for i in range(r):
    k = input().rstrip()
    for j in range(c):
        if k[j] == 'O':
            bomb.add((i,j))

dp = [0,bomb, all_bomb]

for i in range(3,n+1):
    if i%2 == 0:
        dp.append(all_bomb)
    else:
        splash = set()
        for j in dp[i-2]:
            splash.add(j)
            for k in range(4):
                y, x = j[0]+dy[k], j[1]+dx[k]
                if y < 0 or y >= r or x < 0 or x >= c:
                    continue
                splash.add((y,x))
        dp.append(dp[i-1]-splash)

result = []
for i in range(r):
    line = ''
    for j in range(c):
        line += '.'
    result.append(line)

for i in dp[n]:
    result[i[0]] = result[i[0]][:i[1]] + 'O' + result[i[0]][i[1]+1:]

for i in result:
    print(i)