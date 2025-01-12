# 수열의 합

import sys

input = sys.stdin.readline
n, l = map(int, input().split())
s = 0
count = l
is_answer = False
for i in range(l, 101):
    temp = n - (i * (i-1))//2
    if temp >= 0 and temp / i == temp // i:
        s = temp // i
        count = i
        is_answer = True
        break
    
if is_answer:
    for i in range(count):
        print(s+i, end=' ')
else:
    print(-1)
