# 동전

t = int(input())

for i in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1
    for j in range(m+1):
        for k in coin:
            if j - k >= 0:
                if dp[j] == 0:
                    dp[j] = dp[j-k]
                else:
                    dp[j] += dp[j-k]
    print(dp[m])