# ACM Craft

import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, k = map(int, input().split())

    times = [0] + list(map(int, input().split()))

    g = [[] for _ in range(n+1)]
    g_count = [-1] + [0 for _ in range(n)]
    dp = [0 for _ in range(n+1)]

    for __ in range(k):
        a, b = map(int, input().split())
        g[a].append(b)
        g_count[b] += 1

    w = int(input().rstrip())
    q = deque()
    for i in range(1, len(g_count)):
        if g_count[i] == 0:
            dp[i] = times[i]
            q.append(i)
    while q:
        s = q.popleft()
        for m in g[s]:
            dp[m] = max(dp[m], dp[s] + times[m])
            g_count[m] -= 1
            if g_count[m] == 0:
                q.append(m)
    print(dp[w])






#### 1차 검색 완료(1.8) ####
# import sys
# from collections import deque


# input = sys.stdin.readline

# t = int(input().rstrip())

# for _ in range(t):
#     n, k = map(int, input().split())
#     build = [[] for __ in range(n+1)]
#     times = [0] + list(map(int, input().split()))
#     phase = [0] * (n+1)
#     dp = [0] * (n+1)
#     for __ in range(k):
#         a, b = map(int, input().split())
#         build[a].append(b)
#         phase[b] += 1
#     goal = int(input().rstrip())
#     q = deque()
#     for i in range(1, n+1):
#         if phase[i] == 0:
#             q.append(i)
#             dp[i] = times[i]
#     while q:
#         now = q.popleft()
#         for i in build[now]:
#             dp[i] = max(dp[i], dp[now] + times[i])
#             phase[i] -= 1
#             if phase[i] == 0:
#                 q.append(i)
#     print(dp[goal])





# 문제를 잘못 이해함 -> 연결된 건물을 다 지어야 그 다음 건물을 지을 수 있는 줄 모름, 하나만 지어도 되는줄.. 다익스트라..
# import sys
# import heapq
# from collections import deque

# input = sys.stdin.readline

# t = int(input().rstrip())

# for _ in range(t):
#     n, k = map(int, input().split())
#     total = [float('inf') for __ in range(n+1)]
#     times = [0] + list(map(int, input().split()))
#     build = [[] for __ in range(n+1)]
#     for i in range(k):
#         a, b = map(int, input().split())
#         build[b].append((a, times[a]))
#     goal = int(input().rstrip())
#     q = []
#     heapq.heappush(q, (0, goal))
#     total[goal] = 0
#     while q:
#         dist, now = heapq.heappop(q)

#         if total[now] < dist:
#             continue

#         for i in build[now]:
#             if dist + i[1] < total[i[0]]:
#                 total[i[0]] = dist + i[1]
#                 heapq.heappush(q, (dist + i[1], i[0]))
    
#     result = []
#     qq = deque()
#     qq.append(goal)
#     while qq:
#         j = qq.popleft()
#         if not build[j]:
#             result.append(j)
#             continue
#         for l in build[j]:
#             qq.append(l[0])
    
#     answer = float('inf')
#     for r in set(result):
#         answer = min(total[r], answer)
    
#     print("result", set(result))
#     print("total", total)
#     print("answer", answer+times[goal])
