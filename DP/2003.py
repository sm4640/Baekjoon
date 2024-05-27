# 수들의 합 2

n, m = map(int, input().split())

seq = list(map(int, input().split()))

now = 0
count = 0
remove = -1
for i in range(n):
    now += seq[i]
    if now == m:
        count += 1
        continue
    elif now > m:
        for j in range(remove+1, i):
            now -= seq[j]
            if now < m:
                remove = j
                break
            elif now == m:
                count += 1
                remove = j
                break
        else:
            remove = i-1
print(count)