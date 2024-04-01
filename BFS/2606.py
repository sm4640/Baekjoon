# 바이러스

from collections import deque

c = int(input())
n = int(input())

com = [[] for _ in range(c+1)]
check = [0] * (c+1)

for i in range(n):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

q = deque()
q.append(1)

while q:
    i = q.popleft()
    for num in com[i]:
        if check[num] == 0:
            q.append(num)
            check[num] = 1

check[1] = 0
print(check.count(1))