# 친구

import sys

input = sys.stdin.readline

n = int(input().rstrip())

g = [set() for _ in range(n+1)]

count = [0] * (n+1)

for i in range(1,n+1):
    line = input().rstrip()
    for j in range(len(line)):
        if line[j] == 'Y':
            g[i].add(j+1)

for i in range(1,n+1):
    friends = set()
    friends = friends | g[i]
    for j in g[i]:
        friends = friends | g[j]
    friends = friends - {i}
    count[i] = len(friends)

print(max(count))