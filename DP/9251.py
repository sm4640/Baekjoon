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


# LCS (3달 후 또 품 -> 이게 좀 더 빠름)

s1 = input()
s2 = input()

dp = [[0] * len(s1) for _ in range(len(s2))]

if s1[0] == s2[0]:
    dp[0][0] = 1

for i in range(1, len(s1)):
    if dp[0][i-1] == 0:
        if s2[0] == s1[i]:
            dp[0][i] = 1
    else:
        dp[0][i] = 1

for i in range(1, len(s2)):
    if dp[i-1][0] == 0:
        if s1[0] == s2[i]:
            dp[i][0] = 1
    else:
        dp[i][0] = 1

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(s2)-1][len(s1)-1])