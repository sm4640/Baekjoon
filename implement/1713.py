# 후보 추천하기

import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())
r = int(input().rstrip())
recommends = list(map(int, input().split()))
q = []
s = {i:0 for i in range(1, 101)}
for i in range(len(recommends)):
    if s[recommends[i]] == 0:
        s[recommends[i]] += 1
        if len(q) < n:
            heapq.heappush(q, (s[recommends[i]], i, recommends[i]))
        else:
            a, b, c = heapq.heapreplace(q, (s[recommends[i]], i, recommends[i]))
            s[c] = 0
    else:
        for j in range(len(q)):
            if q[j][2] == recommends[i]:
                s[q[j][2]] += 1
                q[j] = (s[q[j][2]], q[j][1], q[j][2])
                heapq.heapify(q)
                break
result = []
for i in q:
    result.append(i[2])
print(*sorted(result))