# 트리의 부모 찾기

from collections import deque

n = int(input())

node = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
visited[1] = -1
q = deque()

for i in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

q.append(1)
while q:
    p = q.popleft()
    for i in node[p]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = p
        else:
            visited[p] = i

for i in range(2, n+1):
    print(visited[i])



# 첫 시도
# import sys
# sys.setrecursionlimit(10000)

# n = int(input())

# g = {}
# p_g = [0 for _ in range(n+1)]
# p_g[1] = -1
# visited = [False for i in range(n+1)]
# for i in range(n-1):
#     a, b = map(int, input().split())
#     if g.get(a,0):
#         g[a].append(b)
#     else:
#         g[a] = [b]
#     if g.get(b,0):
#         g[b].append(a)
#     else:
#         g[b] = [a]

# def dfs(node):
#     if visited[node] == True:
#         return
#     visited[node] = True
#     for j in g[node]:
#         if p_g[j] == 0:
#             p_g[j] = node
#             dfs(j)
#         else:
#             continue

# dfs(1)

# for i in range(2, len(p_g)):
#     print(p_g[i])