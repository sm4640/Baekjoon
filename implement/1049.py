# 기타줄

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

min_pack = float('inf')
min_one = float('inf')
min_table = [0 for _ in range(7)]
for i in range(m):
    p, o = map(int, input().split())
    min_pack = min(min_pack, p)
    min_one = min(min_one, o)

for i in range(1,7):
    now = min_one * i
    min_table[i] = min(min_pack, now)

a = (n//6) * min_table[6]
b = min_table[n%6]

print(a+b)