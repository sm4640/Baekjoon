# 행렬

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [[int(k) for k in input().rstrip()] for _ in range(n)]
b = [[int(k) for k in input().rstrip()] for _ in range(n)]

def flip(i, j):
    for k in range(3):
        for l in range(3):
            a[i+k][j+l] = 1 - a[i+k][j+l]

def sol():
    if a == b:
        return 0
    count = 0
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                flip(i, j)
                count += 1
            if a == b:
                return count
    return -1

print(sol())