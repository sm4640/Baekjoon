# 패션왕 신해빈
from collections import Counter

case_n = int(input())
totals = []

for i in range(case_n):
    total = 1
    names = []
    types = []
    types_n = int(input())
    for _ in range(types_n):
        clothes = input().split()
        names.append(clothes[0])
        types.append(clothes[1])
    types_count = Counter(types)
    for key in types_count.keys():
        total *= (types_count[key] + 1)
    total -= 1
    totals.append(total)

for i in range(len(totals)):
    print(totals[i])