# 부녀회장이 될테야

t = int(input())

dp = [[0] * 15 for _ in range(15)]

for i in range(1,15):
    dp[0][i] = i
for i in range(15):
    dp[i][1] = 1

for k in range(1,15):
    for n in range(2,15):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

for i in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])
