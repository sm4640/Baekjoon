# 가장 큰 증가하는 부분 수열

n = int(input())

a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))