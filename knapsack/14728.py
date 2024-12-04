# 벼락치기

import sys

input = sys.stdin.readline

n, t = map(int, input().split())

ks = [-1]
ss = [-1]

for i in range(n):
    k, s = map(int, input().split())
    ks.append(k)
    ss.append(s)

dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if j >= ks[i]:
            dp[i][j] = max(dp[i-1][j-ks[i]] + ss[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[i][t])