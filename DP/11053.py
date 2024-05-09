# 가장 긴 증가하는 부분 수열

n = int(input())

lst = list(map(int, input().split()))

dp = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i-1, -1, -1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))