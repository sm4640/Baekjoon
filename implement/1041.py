# 주사위

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().rstrip())

num = list(map(int, input().split()))

if n == 1:
    print(sum(num) - max(num))
else:
    total = (n**2) + ((n-1)**2)*4
    side2_count = ((n-2)*4 + (n-1)*4)
    side3_count = 4
    side1_count = total - side2_count - side3_count
    min_sum = float('inf')
    for i in range(6):
        picks = [k for k in range(6) if k != 5-i and k != i]
        now = float('inf')
        com = combinations(picks, 2)
        for j in com:
            if j[0] + j[1] == 5:
                continue
            now = min(num[j[0]]+num[j[1]]+num[i], now)
        min_sum = min(min_sum, now)
    side3 = min_sum * side3_count

    min_sum = float('inf')
    for i in range(6):
        picks = [num[k] for k in range(6) if k != 5-i and k != i]
        now = min(picks)
        min_sum = min(min_sum, now+num[i])
    side2 = min_sum * side2_count

    if side1_count > 0:
        side1 = min(num) * side1_count
    else:
        side1 = 0
    print(side1 + side2 + side3)