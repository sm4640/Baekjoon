# 다리 놓기

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    son, mom = 1, 1
    for j in range(m, m-n, -1):
        print("j: ", j)
        son *= j
    for k in range(n, 0, -1):
        print("k: ", k)
        mom *= k
    print(son//mom)



















# t = int(input())

# for _ in range(t):
#     n,m = map(int, input().split())
#     dividend = 1
#     for i in range(n):
#         dividend *= m-i
#     divisor = 1
#     for i in range(n,0,-1):
#         divisor *= i
#     print(dividend // divisor)



















