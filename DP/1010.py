# 다리 놓기

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    dividend = 1
    for i in range(n):
        dividend *= m-i
    divisor = 1
    for i in range(n,0,-1):
        divisor *= i
    print(dividend // divisor)
