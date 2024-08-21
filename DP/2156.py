# 포도주 시식

n = int(input())

dp = [0] * n

podoju = []
for i in range(n):
    podoju.append(int(input()))

if n == 1:
    print(podoju[0])
elif n == 2:
    print(podoju[0] + podoju[1])
elif n == 3:
    print(max(podoju[0] + podoju[1], podoju[1] + podoju[2], podoju[1] + podoju[2]))
else:
    dp[0] = podoju[0]
    dp[1] = podoju[0] + podoju[1]
    dp[2] = max(dp[1], podoju[0] + podoju[2], podoju[1] + podoju[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + podoju[i-1] + podoju[i], dp[i-2] + podoju[i], dp[i-1])
    print(max(dp))