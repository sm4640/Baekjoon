# 동전 1

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(1,k+1):
        dp[j] = dp[j] + (dp[j-coin] if j-coin >= 0 else 0)

print(dp[k])