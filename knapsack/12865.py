# 평범한 배낭

n, k = map(int, input().split())

w = ['-']
v = ['-']
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    i_w, i_v = map(int, input().split())
    w.append(i_w)
    v.append(i_v)

for i in range(1,n+1):
    for s in range(1,k+1):
        if s >= w[i]:
            dp[i][s] = max(dp[i-1][s], dp[i-1][s-w[i]]+v[i])
        else:
            dp[i][s] = dp[i-1][s]

print(dp[n][s])





# biggest = 0
# obj = []

# for i in range(n):
#     w, v = map(int, input().split())
#     obj.append((w,v))

# visited = [False] * len(obj)
# stack = []

# def dfs():
#     global biggest
#     if sum([s[0] for s in stack]) > k:
#         biggest = max(sum([s[1] for s in stack][:-1]), biggest)
#         return
#     elif len(stack) == len(obj):
#         biggest = max(sum([s[1] for s in stack]), biggest)
#         return
    
#     for i in range(len(obj)):
#         if visited[i]:
#             continue
#         stack.append(obj[i])
#         visited[i] = True
#         dfs()
#         stack.pop()
#         visited[i] = False

# dfs()

# print(biggest)