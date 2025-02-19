# 제곱수 찾기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

table = []
result = -1
for _ in range(n):
    table.append(input().rstrip())

for i in range(n):
    for j in range(m):
        for a in range(-n,n):
            for b in range(-m,m):
                if a == 0 and b == 0:
                    continue
                now = ''
                now_y, now_x = i, j
                while 0 <= now_y < n and 0 <= now_x < m:
                    now += table[now_y][now_x]
                    now_y += a
                    now_x += b
                    if int(int(now)**(0.5))**2 == int(now):
                        result = max(result, int(now))

print(result)






# 1차 검색 완료(2.9)
# import sys
# import math

# input = sys.stdin.readline

# n, m  = map(int, input().split())

# table = [input().rstrip() for _ in range(n)]

# max_number = -1
# for i in range(n):
#     for j in range(m):
#         for a in range(-n, n):
#             for b in range(-m, m):
#                 now_y, now_x = i, j
#                 number = ''
#                 if a == 0 and b == 0:
#                     continue
#                 while 0 <= now_y < n and 0 <= now_x < m:
#                     number += table[now_y][now_x]
#                     if int(math.sqrt(int(number))) ** 2 == int(number):
#                         max_number = max(max_number, int(number))
#                     now_y += a
#                     now_x += b
# print(max_number)