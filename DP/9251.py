# LCS

a = input()
b = input()

dp = [[0]*len(a) for _ in range(len(b))]

if a[0] == b[0]:
    dp[0][0] = 1

for i in range(1,len(b)):
    if a[0] == b[i]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1,len(a)):
    if b[0] == a[i]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1,len(b)):
    for j in range(1,len(a)):
        if b[i] == a[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(b)-1][len(a)-1])