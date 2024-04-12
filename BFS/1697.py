# 숨바꼭질
from collections import deque

n, k = map(int, input().split())

walk = [-1, 1]
tel = 2

check = [0] * 100001

q = deque()
q.append(n)
check[n] = 1

while q:
    next = q.popleft()
    
    for i in range(2):
        a = next + walk[i]
        if a >= 0 and a <= 100000 and check[a] == 0:
            q.append(a)
            check[a] = check[next] + 1
    b = next * tel
    if b >= 0 and b <= 100000 and check[b] == 0:
        q.append(b)
        check[b] = check[next] + 1

print(check[k] - 1)


# 1차 코드
# from collections import deque


# n, k = map(int, input().split())

# walk = [-1, 1]
# tel = 2

# count = 0
# now_count = 0
# q = deque()
# q.append((n, count))

# while q:
#     next, count = q.popleft()
#     if count == now_count:
#         now_count += 1
    
#     if next == k:
#         break

#     count += 1
    
#     for i in range(2):
#         a = next + walk[i]
#         q.append((a, count))
#     b = next * tel
#     q.append((b, count))
    
# print(now_count-1)