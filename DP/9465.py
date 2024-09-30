# 스티커

t = int(input())

for i in range(t):
    n = int(input())
    st = [list(map(int, input().split())) for _ in range(2)]
    st = [[0,0] + st[0], [0,0] + st[1]]
    dp = [[0]*(n+2) for _ in range(2)]
    for i in range(2,n+2):
        dp[0][i] = max(dp[1][i-2] + st[0][i], dp[1][i-1] + st[0][i])
        dp[1][i] = max(dp[0][i-2] + st[1][i], dp[0][i-1] + st[1][i])

    print(max(max(dp[0]), max(dp[1])))