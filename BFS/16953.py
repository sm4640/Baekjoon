# A -> B
from collections import deque

a, b = map(int, input().split())

q = deque()

count = 0
q.append((count, a))

while q:
    ncount, na = q.popleft()
    if ncount != count:
        count += 1

    if na*2 > b:
        continue
    elif na*2 == b:
        count += 1
        print(count+1)
        break
    else:
        q.append((count+1, na*2))

    if na*10+1 > b:
        continue
    elif na*10+1 == b:
        count += 1
        print(count+1)
        break
    else:
        q.append((count+1, na*10+1))

else:
    print(-1)